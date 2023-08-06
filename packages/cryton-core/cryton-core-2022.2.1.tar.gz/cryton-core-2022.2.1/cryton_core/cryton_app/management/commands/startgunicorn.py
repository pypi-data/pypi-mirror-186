from threading import Thread
from django.core.management.base import BaseCommand
from gunicorn.app.base import BaseApplication

from cryton_core.asgi import application
from cryton_core.lib.util.logger import logger_object


class GunicornApplication(BaseApplication):

    def __init__(self, app, options=None):
        self.options = options or {}
        self.application = app
        super().__init__()

    def init(self, parser, opts, args):
        pass

    def load_config(self):
        config = {key: value for key, value in self.options.items()
                  if key in self.cfg.settings and value is not None}
        for key, value in config.items():
            self.cfg.set(key.lower(), value)

    def load(self):
        return self.application


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument("--bind", type=str, help="ADDRESS:PORT to serve the server at.")
        parser.add_argument("--workers", type=int, help="The NUMBER of worker processes for handling requests.")

    def handle(self, *args, **options):
        hard_options = {
            "bind": options.get("bind", "0.0.0.0:8000"),
            "worker_class": "uvicorn.workers.UvicornWorker",
            "workers": options.get("workers", 2)
        }

        gunicorn_app = GunicornApplication(application, hard_options)

        # Start log_handler in a thread to ensure the logs from multiprocessing aren't missing
        logger_processor_thread = Thread(target=logger_object.log_handler)
        logger_processor_thread.start()

        try:
            gunicorn_app.run()
        finally:  # Ensure the log_handler will stop
            logger_object.log_queue.put(None)
