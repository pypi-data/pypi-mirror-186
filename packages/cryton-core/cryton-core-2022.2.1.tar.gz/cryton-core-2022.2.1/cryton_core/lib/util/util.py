import json
from threading import Thread
from functools import reduce
import copy
from typing import List, Union, Dict
from datetime import datetime, timedelta
import configparser
import pytz
import amqpstorm
from jinja2 import nativetypes, DebugUndefined, StrictUndefined, ChainableUndefined, UndefinedError
import re
import yaml

from cryton_core.etc import config
from cryton_core.lib.util import exceptions, logger, constants

from django.utils import timezone


def convert_to_utc(original_datetime: datetime, time_zone: str = 'utc', offset_aware: bool = False) -> datetime:
    """
    Convert datetime in specified timezone to UTC timezone
    :param original_datetime: datetime to convert
    :param time_zone: timezone of the original datetime (examples: "utc"; "Europe/Prague")
    :param offset_aware: if True, utc_datetime will be offset-aware, else it will be offset-naive
    :return: datetime in UTC timezone
    """
    if not original_datetime.tzinfo:
        original_datetime = pytz.timezone(time_zone).localize(original_datetime, is_dst=None)
        # original_datetime = original_datetime.astimezone(time_zone)

    utc_datetime = original_datetime.astimezone(timezone.utc)
    if not offset_aware:
        return utc_datetime.replace(tzinfo=None)
    return utc_datetime


def convert_from_utc(utc_datetime: datetime, time_zone: str, offset_aware: bool = False) -> datetime:
    """
    Convert datetime in UTC timezone to specified timezone
    :param utc_datetime: datetime in UTC timezone to convert
    :param time_zone: timezone of the new datetime (examples: "utc"; "Europe/Prague")
    :param offset_aware: if True, utc_datetime will be offset-aware, else it will be offset-naive
    :return: datetime with the specified timezone
    """
    if not utc_datetime.tzinfo:
        utc_datetime = pytz.utc.localize(utc_datetime, is_dst=None)

    new_datetime = utc_datetime.astimezone(pytz.timezone(time_zone))
    if not offset_aware:
        return new_datetime.replace(tzinfo=None)
    return new_datetime


# TODO: update to format YY-MM-DD hh:mm:ss, then remove
def parse_delta_to_datetime(time_str: str) -> timedelta:
    try:
        split_hours = time_str.split("h")
        hours = split_hours[0]

        split_minutes = split_hours[1].split("m")
        minutes = split_minutes[0]

        split_seconds = split_minutes[1].split("s")
        seconds = split_seconds[0]

        hours = int(hours)
        minutes = int(minutes)
        seconds = int(seconds)
    except Exception:
        raise exceptions.UserInputError("Invalid delta provided. Correct format is [int]h[int]m[int]s", time_str)

    return timedelta(hours=hours, minutes=minutes, seconds=seconds)


# TODO: move to the cryton_app/util.py
class IgnoreNestedUndefined(ChainableUndefined, DebugUndefined):
    def __getattr__(self, attr: str) -> "IgnoreNestedUndefined":
        self._undefined_name += f'.{attr}'

        return self

    def __getitem__(self, item: str) -> "IgnoreNestedUndefined":
        self._undefined_name += f'[{item}]'

        return self


# TODO: move to StepEx class
def fill_execution_variables(arguments: dict, execution_variables: dict) -> dict:
    """
    Fill Jinja variables in the Step arguments with execution variables.
    :param arguments: Arguments to fill
    :param execution_variables: Execution variables to fill the template with
    :return: Filled arguments
    """
    env = nativetypes.NativeEnvironment(
        undefined=StrictUndefined, block_start_string=constants.BLOCK_START_STRING,
        block_end_string=constants.BLOCK_END_STRING, variable_start_string=constants.VARIABLE_START_STRING,
        variable_end_string=constants.VARIABLE_END_STRING, comment_start_string=constants.COMMENT_START_STRING,
        comment_end_string=constants.COMMENT_END_STRING)

    arguments_template = env.from_string(yaml.safe_dump(arguments))
    try:
        return yaml.safe_load(arguments_template.render(**execution_variables))
    except (yaml.YAMLError, UndefinedError, TypeError) as ex:
        raise exceptions.StepValidationError(f"An error occurred while updating execution variables. {ex}.")


# TODO: move to the cryton_app/util.py
def fill_template(template: str, inventory_variables: dict) -> str:
    """
    Fill Jinja variables in the template with inventory variables.
    :param inventory_variables: Template variables to fill the template with
    :param template: Template to fill
    :return: Filled template
    """
    env = nativetypes.NativeEnvironment(undefined=IgnoreNestedUndefined)

    try:
        plan_template_obj = env.from_string(template)
        filled_template = plan_template_obj.render(**inventory_variables)
    except (TypeError, UndefinedError):
        raise exceptions.ValidationError(f"Template is not a valid jinja template: {template}")

    return filled_template


# TODO: move to the cryton_app/util.py
def parse_inventory(inventory: str) -> dict:
    """
    Reads inventory file (JSON, YAML, INI) and returns it as a dictionary
    :param inventory: Inventory file content
    :return: Inventory variables
    """
    # JSON
    try:
        return json.loads(inventory)
    except json.decoder.JSONDecodeError:
        pass

    # YAML
    try:
        return yaml.safe_load(inventory)
    except yaml.YAMLError:
        pass

    # INI
    try:
        config_parser = configparser.ConfigParser()
        config_parser.read_string(inventory)
        return {section: dict(config_parser.items(section)) for section in config_parser.sections()}
    except configparser.Error:
        pass

    raise ValueError(f"Inventory file must contain data and be of type JSON, YAML, or INI. File: {inventory}")


def split_into_lists(input_list: List, target_number_of_lists: int) -> List[List]:
    """
    Evenly splits list into n lists.
    E.g. split_into_lists([1,2,3,4], 4) returns [[1], [2], [3], [4]].
    :param input_list: object to split
    :param target_number_of_lists: how many lists to split into
    :returns: list of lists containing original items
    """

    quotient, reminder = divmod(len(input_list), target_number_of_lists)
    return [input_list[i * quotient + min(i, reminder):(i + 1) * quotient + min(i + 1, reminder)] for i in
            range(target_number_of_lists)]


def run_executions_in_threads(step_executions: List) -> None:
    """
    Creates new Rabbit connection, distributes step executions into threads and runs the threads.
    To set desired number of threads/process, see "CRYTON_CORE_EXECUTION_THREADS_PER_PROCESS" variable in config.

    :param step_executions: list of step execution objects
    """
    connection_parameters = {"hostname": config.RABBIT_HOST, "username": config.RABBIT_USERNAME,
                             "password": config.RABBIT_PASSWORD, "port": config.RABBIT_PORT}
    with amqpstorm.Connection(**connection_parameters) as connection:
        # Split executions into threads
        thread_lists = split_into_lists(step_executions, config.EXECUTION_THREADS_PER_PROCESS)
        threads = []
        for thread_step_executions in thread_lists:
            new_thread = Thread(target=run_step_executions, args=(connection, thread_step_executions))
            threads.append(new_thread)

        for thread in threads:
            thread.start()

        # Wait for threads to finish
        for thread in threads:
            thread.join()


def run_step_executions(rabbit_connection: amqpstorm.Connection, step_execution_list: List) -> None:
    """
    Creates new Rabbit channel and runs step executions.

    :param rabbit_connection: Rabbit connection
    :param step_execution_list: list of step execution objects to execute
    """
    with rabbit_connection.channel() as channel:
        for step_execution in step_execution_list:
            logger.logger.debug("Running Step Execution in thread", step_execution_id=step_execution.model.id)
            step_execution.execute(channel)


def getitem(obj: Union[List, Dict], key: str):
    """
    Get item from object using key.
    :param obj: Iterable accessible using key
    :param key: Key to use to get (match) Item
    :return: Matched item
    """
    match = re.match(r"^\[[0-9]+]$", key)  # Check if key matches List index.
    if match is not None:
        key = int(match.group()[1:-1])  # Convert List index to int.

    result = None
    if isinstance(key, str) and isinstance(obj, dict):  # Use key to get item from Dict.
        result = obj.get(key)
        if result is None and key.isdigit():  # May be int.
            result = obj.get(int(key))
    elif isinstance(key, int) and isinstance(obj, list):  # Use key to get item from List.
        try:
            result = obj[key]
        except IndexError:
            pass
    return result


def parse_dot_argument(dot_argument: str) -> List[str]:
    """
    Takes a single argument (Dict key) from dot notation and checks if it also contains list indexes.
    :param dot_argument: Dict key from dot notation possibly containing list indexes
    :return: Dict key and possible List indexes
    """
    list_indexes = re.search(r"((\[[0-9]+])+$)", dot_argument)  # Check for List indexes at the argument's end.
    if list_indexes is not None:  # Get each List index in '[index]' format and get index only.
        parsed_list_indexes = re.findall(r"(\[[0-9]+])", list_indexes.group())
        parsed_list_indexes = [index for index in parsed_list_indexes]
        return [dot_argument[0:list_indexes.start()]] + parsed_list_indexes
    return [dot_argument]  # If no List Indexes are present.


def get_from_dict(dict_in: dict, value: str):
    """
    Get value from dict_in dict
    eg:
      dict_in: {'output': {'username': 'admin'}}
      value: '$dict_in.output.username'
      return: 'admin'
    :param value: value defined in template
    :param dict_in: dict_in for this step
    :return: value from dict_in
    """
    dot_args = value.lstrip('$').split('.')  # Get keys using '.' separator.
    all_args = []  # Dict keys and List indexes.
    for dot_arg in dot_args:  # Go through dot_args and separate all args.
        all_args.extend(parse_dot_argument(dot_arg))

    try:
        res = reduce(getitem, all_args, dict_in)
    except KeyError:
        res = None

    return res


def _finditem(obj, key):
    """
    Check if giben key exists in an object
    :param obj: dictionary/list
    :param key: key
    :return: value at the key position
    """
    if key in obj:
        return obj[key]
    for k, v in obj.items():
        if isinstance(v, dict):
            item = _finditem(v, key)
            if item is not None:
                return item


def update_inner(obj: dict, dict_in: dict, startswith: str):
    """

    Update value inside the object with one specified by prefix and path from dict_in
    eg.: $dict_in.test replaces with dict_in.get('test')

    :param obj: Object
    :param dict_in: dict_in dictioanry
    :param startswith: prefix, eg. $
    :return:
    """
    if isinstance(obj, dict):
        for k, v in obj.items():
            if isinstance(v, str):
                if v.startswith(startswith):
                    new_val = get_from_dict(dict_in, v)
                    if new_val is not None:
                        obj.update({k: new_val})
            elif isinstance(v, dict):
                update_inner(v, dict_in, startswith)
            elif isinstance(v, list):
                for value in v:
                    update_inner(value, dict_in, startswith)


def replace_value_in_dict(dict_to_repl: dict,
                          dict_in: dict,
                          startswith: str = '$'):
    """
    Replace value in dictionary
    :param dict_to_repl:
    :param dict_in: dict_in
    :param startswith: prefix
    :return:
    """

    if startswith not in str(dict_to_repl):
        raise ValueError("No value starting with {} in dictionary".format(startswith))
    if dict_in is None:
        # Nothing to replace
        return None
    update_inner(dict_to_repl, dict_in, startswith)


def fill_dynamic_variables(in_dict, var_dict):
    """

    Fill variables in in_dict with var_dict.

    :param in_dict:
    :param var_dict:
    :return:
    """
    in_dict_copy = copy.deepcopy(in_dict)
    update_inner(in_dict_copy, var_dict, '$')

    return in_dict_copy


def get_all_values(input_container):
    """
    Get all values (recursively) from a dict
    :param input_container: input dict or list
    :return: yields elements, use as list(get_all_values(d))
    """
    if isinstance(input_container, dict):
        for value in input_container.values():
            yield from get_all_values(value)
    elif isinstance(input_container, list):
        for item in input_container:
            yield from get_all_values(item)
    else:
        yield input_container


def get_dynamic_variables(in_dict, prefix='$'):
    """
    Get list of dynamic variables for input dict
    :param in_dict:
    :param prefix:
    :return:
    """
    vars_list = list(get_all_values(in_dict))

    for i in vars_list:
        if isinstance(i, str) and i.startswith(prefix):
            yield i


def get_prefixes(vars_list):
    """
    Get list of prefixes from list of dynamic variables
    :param vars_list:
    :return:
    """
    for i in vars_list:
        yield i.split('.')[0].lstrip('$')


def pop_key(in_dict, val):
    """
    Pop key at specified position (eg. 'k1.k2.k3')
    :param in_dict:
    :param val:
    :return: Nothing, changes in_dict inplace
    """
    if type(in_dict) != dict:
        return in_dict
    if type(val) == list and len(val) > 1:
        if len(val) != 2:
            return pop_key(in_dict.get(val[0]), val[1:])
        else:
            return in_dict.get(val[0]).pop(val[1])
    else:
        print(val)
        return in_dict.pop(val[0])


def add_key(in_dict, path, val):
    """
    Add value on specified key position
    :param in_dict: eg. {a: 1, b:2}
    :param path: 'c.d.e'
    :param val: '3
    :return: changes in place, eg. {a:1, b:2, c:{d:{e:3}}}
    """
    first = True
    tmp_dict = {}

    for i in path.split('.')[::-1]:
        if first is True:
            tmp_dict = {i: val}
            first = False
        else:
            tmp_dict = {i: tmp_dict}
    in_dict.update(tmp_dict)


def rename_key(in_dict, rename_from, rename_to):
    """
    Rename key (= move to different place)

    eg.
    in_dict = {a: 1, b: 2, c: {d: 3}}
    rename_from = 'c.d'
    rename_to = 'e.f.g'

    result = {a: 1, b: 2, e: {f: {g: 3}}}

    :param in_dict:
    :param rename_from:
    :param rename_to:
    :return: Changes inplace
    :raises KeyError, if rename_from key is not found
    """
    new_val = pop_key(in_dict, rename_from.split('.'))
    add_key(in_dict, rename_to, new_val)


def get_logs() -> list:
    """
    Retrieve logs from log file.
    :return: Parsed Logs
    """
    log_file_path = config.LOG_FILE_PATH_DEBUG if config.DEBUG else config.LOG_FILE_PATH
    with open(log_file_path, "r") as log_file:
        return [log.rstrip(", \n") for log in log_file]
