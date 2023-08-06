import json
import time
from threading import Thread
from multiprocessing import Process, Event

import amqpstorm

from cryton_core.lib.util import constants, logger, states, event, rabbit_client
from cryton_core.lib.models import stage, plan, step, run
from cryton_core.etc import config

from cryton_core.cryton_app.models import CorrelationEventModel

from cryton_core.lib.services.scheduler import SchedulerService
from django.utils import timezone


class ChannelConsumer:
    def __init__(self, identifier: int, connection: amqpstorm.Connection, queues: dict):
        self._id = identifier
        self._channel = connection.channel()

        self._channel.basic.qos(1)
        for queue, callback in queues.items():  # Consume on each queue.
            self._channel.queue.declare(queue)
            self._channel.basic.consume(callback, queue)

    def start(self):
        logger.logger.debug("Channel consumer started.", id=self._id)
        while not self._channel.is_closed:
            try:
                self._channel.start_consuming()

            except amqpstorm.AMQPConnectionError as ex:
                logger.logger.debug("Channel consumer encountered a connection error.", id=self._id, error=str(ex))
                break

            except Exception as ex:  # If any uncaught exception occurs, channel consumer will still work
                logger.logger.warning("Channel consumer encountered an error.", id=self._id, error=str(ex))

        logger.logger.debug("Channel consumer stopped.", id=self._id)


class Consumer:
    def __init__(self, identifier: int, queues: dict, channel_consumer_count: int):
        """
        Consumer takes care of the connection between Core and RabbitMQ server and launching callbacks for the
        defined queues.
        :param identifier: consumer ID
        :param queues: Queues to consume
        :param channel_consumer_count: How many consumers to use for queues
            (higher == faster == heavier processor usage)
        """
        self._id = identifier
        self._queues = queues
        self._channel_consumer_count = channel_consumer_count if channel_consumer_count > 0 else 1

        self._hostname = config.RABBIT_HOST
        self._port = config.RABBIT_PORT
        self._username = config.RABBIT_USERNAME
        self._password = config.RABBIT_PASSWORD

        self._stopped = Event()
        self._connection: amqpstorm.Connection or None = None

    def start(self) -> None:
        """
        Establish connection, start channel consumers in thread and keep self alive.
        :return: None
        """
        logger.logger.debug("Consumer started.", id=self._id, channel_consumer_count=self._channel_consumer_count)
        self._stopped.clear()

        try:
            while not self._stopped.is_set():  # Keep self and connection alive and check for stop.
                try:
                    if self._update_connection():
                        self._start_channel_consumers()

                except amqpstorm.AMQPConnectionError:
                    pass

                time.sleep(5)
        except KeyboardInterrupt:
            self.stop()

    def stop(self) -> None:
        """
        Stop Consumer (self). Close connection and its channels.
        :return: None
        """
        if self._stopped.is_set():
            return

        logger.logger.debug("Stopping Consumer.", id=self._id)
        self._stopped.set()

        if self._connection is not None and self._connection.is_open:  # Close connection and its channels.
            logger.logger.debug("Closing channels.")
            print("Closing connection and it's channels..")
            for channel in list(self._connection.channels.values()):
                channel.close()
            logger.logger.debug("Closing connection.")
            self._connection.close()

        logger.logger.debug("Consumer stopped.", id=self._id)

    def _update_connection(self) -> bool:
        """
        Check existing connection for errors and optionally reconnect.
        :return: True if connection was updated
        :raises: amqpstorm.AMQPConnectionError if connection can't be established
        """
        try:  # If connection is missing or there is some other problem, raise exception
            if self._connection is None:
                raise amqpstorm.AMQPConnectionError("Connection does not exist.")

            if not self._connection.is_open:
                raise amqpstorm.AMQPConnectionError("Connection is closed.")

            self._connection.check_for_errors()

            return False

        except amqpstorm.AMQPError as ex:  # Try to establish connection on error
            logger.logger.warning("No connection to RabbitMQ server", error=str(ex))
            self._connection = amqpstorm.Connection(self._hostname, self._username, self._password, self._port)
            logger.logger.info("Connection to RabbitMQ server established")

        return True

    def _start_channel_consumers(self) -> None:
        """
        Start channel consumers in threads.
        :return: None
        """
        logger.logger.debug("Starting channel consumers", channel_consumer_count=self._channel_consumer_count)
        for i in range(self._channel_consumer_count):
            channel_consumer = ChannelConsumer(i + 1, self._connection, self._queues)
            thread = Thread(target=channel_consumer.start, name=f"Thread-{i}-consumer")
            thread.start()


class Listener:
    def __init__(self):
        """
        Listener.
        """
        self._consumers = {}
        self.consumers_count = config.CPU_CORES

        self._stopped = Event()
        self.scheduler = SchedulerService()

        self.queues = {
            config.Q_ATTACK_RESPONSE_NAME: self.step_response_callback,
            config.Q_AGENT_RESPONSE_NAME: self.step_response_callback,
            config.Q_EVENT_RESPONSE_NAME: self.event_callback,
            config.Q_CONTROL_REQUEST_NAME: self.control_request_callback
        }

    def start(self) -> None:
        """
        Start consumers and keep self alive.
        :return: None
        """
        print("Starting RabbitMQ listener")
        self._create_consumers()
        self._start_consumers()
        print("Started RabbitMQ listener")
        logger.logger.info("Started RabbitMQ listener")
        try:
            while not self._stopped.is_set():
                time.sleep(5)
        except KeyboardInterrupt:
            pass

        self.stop()

    def stop(self) -> None:
        """
        Stop Listener and it's Consumers.
        :return: None
        """
        print("Stopping RabbitMQ listener")
        for consumer, consumer_process in self._consumers.items():
            try:
                consumer.stop()
            except Exception as ex:
                logger.logger.warning("Unable to stop Consumer", error=str(ex))
                consumer_process.kill()

        self.scheduler.scheduler.shutdown()

        self._stopped.set()
        print("Stopped RabbitMQ listener")
        logger.logger.info("Stopped RabbitMQ listener")

    def _create_consumers(self) -> None:
        """
        Create consumers and their processes.
        :return: None
        """
        for i in range(self.consumers_count):
            consumer = Consumer(i, self.queues, config.EXECUTION_THREADS_PER_PROCESS)
            consumer_process = Process(target=consumer.start)
            self._consumers[consumer] = consumer_process

    def _start_consumers(self) -> None:
        """
        Start each consumer in process.
        :return: None
        """
        for consumer_process in self._consumers.values():
            consumer_process.start()

    def step_response_callback(self, message: amqpstorm.Message) -> None:
        """
        Callback for processing Step execution responses.
        :param message: Received RabbitMQ message
        :return: None
        """
        logger.logger.debug("Received Step response callback", correlation_id=message.correlation_id)
        message.ack()

        # Get correlation event object from DB
        correlation_id = message.correlation_id
        try:
            correlation_event_obj = self._get_correlation_event(correlation_id)
        except CorrelationEventModel.DoesNotExist:
            logger.logger.warning("Received nonexistent correlation_id", correlation_id=correlation_id)
            return

        # Create execution object and delete the correlation event
        step_ex_obj = step.StepExecution(step_execution_id=correlation_event_obj.step_execution_id)
        correlation_event_obj.delete()

        # Process finished execution
        message_body = json.loads(message.body)
        logger.logger.info("Step execution finished", step_execution_id=step_ex_obj.model.id,
                           message_body=message_body)

        step_ex_obj.postprocess(message_body)  # Save result, output, sessions, etc.
        step_ex_obj.ignore_successors()  # Ignore successors depending on the result
        event.Event({"step_execution_id": step_ex_obj.model.id}).handle_finished_step()  # Handle FINISHED states

        # Check if execution is being paused, otherwise execute successors if StepExecution is in FINISHED state
        if plan.PlanExecution(plan_execution_id=step_ex_obj.model.stage_execution.plan_execution_id).\
                state == states.PAUSING:
            self._handle_pausing(step_ex_obj)
        elif step_ex_obj.state == states.FINISHED:  # State of successors is set to IGNORE in ignore_successors if parent step state is not FINISHED
            step_ex_obj.execute_successors()

    @staticmethod
    def event_callback(message: amqpstorm.Message) -> None:
        """
        Callback for processing events.
        :param message: Received RabbitMQ message
        :return: None
        """
        logger.logger.debug("Received event callback", correlation_id=message.correlation_id)
        message.ack()

        message_body = json.loads(message.body)
        try:
            event_t = message_body[constants.EVENT_T]
            event_v = message_body[constants.EVENT_V]
        except (TypeError, KeyError):
            logger.logger.warn("Event must contain event_t and event_v!")
            return

        if event_t == constants.EVENT_TRIGGER_STAGE:
            event.Event(event_v).trigger_stage()
        elif event_t == constants.EVENT_STEP_EXECUTION_ERROR:
            event.Event(event_v).handle_finished_step()
        else:
            logger.logger.warn("Nonexistent event received", event_t=event_t)

    def control_request_callback(self, message: amqpstorm.Message) -> None:
        """
        Callback for processing control requests.
        :param message: Received RabbitMQ message
        :return: None
        """
        logger.logger.debug("Received control request callback", correlation_id=message.correlation_id)
        message.ack()

        message_body = json.loads(message.body)
        result = -1
        try:
            event_t = message_body[constants.EVENT_T]
            event_v = message_body[constants.EVENT_V]
        except (TypeError, KeyError):
            logger.logger.warn("Control request must contain event_t and event_v!")

        else:
            if event_t == constants.EVENT_UPDATE_SCHEDULER:
                result = event.Event(event_v).update_scheduler()
            else:
                logger.logger.warn("Nonexistent event received", event_t=event_t)

        response = {constants.RETURN_VALUE: result}
        self._send_response(message, response)

    @staticmethod
    def _get_correlation_event(correlation_id: str) -> CorrelationEventModel:
        """
        Find correlation event.
        :param correlation_id: ID of the correlation event
        :return: correlation event
        :raises: CorrelationEventModel.DoesNotExist
        """
        # The correlation event may not be created yet, give it some time
        timeout = time.time() + config.DEFAULT_RPC_TIMEOUT
        while time.time() < timeout:
            try:
                return CorrelationEventModel.objects.get(correlation_id=correlation_id)
            except CorrelationEventModel.DoesNotExist:
                time.sleep(3)

        raise CorrelationEventModel.DoesNotExist()

    @staticmethod
    def _handle_pausing(step_ex_obj: step.StepExecution) -> None:
        """
        Check for PAUSED states.
        :param step_ex_obj: StepExecution object to check
        :return: None
        """
        logger.logger.info("Handling pause", step_execution_id=step_ex_obj.model.id)

        # Pause Stage execution and successors only if it's in the PAUSING state
        stage_ex_obj = stage.StageExecution(stage_execution_id=step_ex_obj.model.stage_execution_id)
        if stage_ex_obj.state == states.PAUSING:
            step_ex_obj.pause_successors()  # Pause all successors so they can be executed after UNPAUSE

            # If any Steps are still running/starting, no execution can be paused
            if stage_ex_obj.model.step_executions.all().exclude(state__in=[states.STARTING, states.RUNNING]).exists():
                return

            stage_ex_obj.state = states.PAUSED
            stage_ex_obj.pause_time = timezone.now()
            logger.logger.info("Stage execution paused", stage_execution_id=stage_ex_obj.model.id)

        # Check if Plan execution should be paused since the Stage execution could have finished
        plan_ex_obj = plan.PlanExecution(plan_execution_id=stage_ex_obj.model.plan_execution_id)
        if plan_ex_obj.state == states.PAUSING and not plan_ex_obj.model.stage_executions.all()\
                .exclude(state__in=states.PLAN_STAGE_PAUSE_STATES).exists():
            plan_ex_obj.state = states.PAUSED
            plan_ex_obj.pause_time = timezone.now()
            logger.logger.info("Plan execution paused", stage_execution_id=stage_ex_obj.model.id)

            run_obj = run.Run(run_model_id=plan_ex_obj.model.run_id)
            if run_obj.state == states.PAUSING and not run_obj.model.plan_executions.all()\
                    .exclude(state__in=states.PLAN_FINAL_STATES + states.PLAN_UNPAUSE_STATES).exists():
                run_obj.state = states.PAUSED
                run_obj.pause_time = timezone.now()
                logger.logger.info("Run paused", stage_execution_id=stage_ex_obj.model.id)

    @staticmethod
    def _send_response(original_message: amqpstorm.Message, message_body: dict) -> None:
        """
        Send a response to `reply_to` from the original message.
        :param original_message: Received message
        :param message_body: Message content
        :return: None
        """
        properties = {'correlation_id': original_message.correlation_id}
        with rabbit_client.Client(original_message.channel) as client:
            client.send_message(original_message.reply_to, message_body, properties)
