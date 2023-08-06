from os import getenv, sched_getaffinity, path, mkdir
from dotenv import load_dotenv


APP_DIRECTORY = getenv('CRYTON_CORE_APP_DIRECTORY', path.expanduser("~/.local/cryton-core/"))

load_dotenv(path.join(APP_DIRECTORY, ".env"))

REPORT_DIRECTORY = path.join(APP_DIRECTORY, "reports/")
EVIDENCE_DIRECTORY = path.join(APP_DIRECTORY, "evidence/")
LOG_DIRECTORY = path.join(APP_DIRECTORY, "log/")

for file_path in [APP_DIRECTORY, REPORT_DIRECTORY, EVIDENCE_DIRECTORY, LOG_DIRECTORY]:
    if not path.exists(file_path):
        mkdir(file_path)

LOG_FILE_PATH = path.join(LOG_DIRECTORY, "cryton-core.log")
LOG_FILE_PATH_DEBUG = path.join(LOG_DIRECTORY, "cryton-core-debug.log")

MISFIRE_GRACE_TIME = 180

TIME_ZONE = getenv('CRYTON_CORE_TZ')

DEBUG = True if getenv('CRYTON_CORE_DEBUG').lower() == 'true' else False

DB_NAME = getenv('CRYTON_CORE_DB_NAME')
DB_USERNAME = getenv('CRYTON_CORE_DB_USERNAME')
DB_PASSWORD = getenv('CRYTON_CORE_DB_PASSWORD')
DB_HOST = getenv('CRYTON_CORE_DB_HOST')
DB_PORT = int(getenv('CRYTON_CORE_DB_PORT'))

RABBIT_USERNAME = getenv('CRYTON_CORE_RABBIT_USERNAME')
RABBIT_PASSWORD = getenv('CRYTON_CORE_RABBIT_PASSWORD')
RABBIT_HOST = getenv('CRYTON_CORE_RABBIT_HOST')
RABBIT_PORT = int(getenv('CRYTON_CORE_RABBIT_PORT'))

Q_ATTACK_RESPONSE_NAME = getenv('CRYTON_CORE_Q_ATTACK_RESPONSE')
Q_AGENT_RESPONSE_NAME = getenv('CRYTON_CORE_Q_AGENT_RESPONSE')
Q_EVENT_RESPONSE_NAME = getenv('CRYTON_CORE_Q_EVENT_RESPONSE')
Q_CONTROL_REQUEST_NAME = getenv('CRYTON_CORE_Q_CONTROL_REQUEST')

# available cores to the application
try:
    CPU_CORES = int(getenv('CRYTON_CORE_CPU_CORES', 3))
except ValueError:
    CPU_CORES = len(sched_getaffinity(0))
EXECUTION_THREADS_PER_PROCESS = int(getenv('CRYTON_CORE_EXECUTION_THREADS_PER_PROCESS', 7))

DEFAULT_RPC_TIMEOUT = int(getenv('CRYTON_CORE_DEFAULT_RPC_TIMEOUT'))

DJANGO_API_ROOT_URL = 'api/'
DJANGO_ALLOWED_HOSTS = getenv('CRYTON_CORE_API_ALLOWED_HOSTS')
DJANGO_ALLOWED_HOSTS = [] if DJANGO_ALLOWED_HOSTS == '' else DJANGO_ALLOWED_HOSTS.split(' ')
DJANGO_STATIC_ROOT = getenv('CRYTON_CORE_API_STATIC_ROOT')
DJANGO_SECRET_KEY = getenv('CRYTON_CORE_API_SECRET_KEY')
DJANGO_USE_STATIC_FILES = True if getenv('CRYTON_CORE_API_USE_STATIC_FILES').lower() == 'true' else False
UPLOAD_DIRECTORY_RELATIVE = "uploads/"
