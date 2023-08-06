# coding=utf-8

import os
import stat
import sys
import json
import datetime
import traceback
import socket
import logging
from logging.handlers import RotatingFileHandler

from kafka import KafkaProducer

from applyx.conf import settings
from applyx.utils import get_log_dir


FLAGS = os.O_WRONLY | os.O_CREAT
MODE = stat.S_IRUSR | stat.S_IWUSR


class LogFormatter(logging.Formatter):
    def format(self, record):
        record.modulepath = record.pathname[len(settings.WORKSPACE) + 1 :]
        return super().format(record)


class KafkaLoggingHandler(logging.Handler):
    def __init__(self):
        super().__init__()
        config = getattr(settings, "KAFKA", None)
        if config is None:
            raise Exception("missing settings for KAFKA")

        self.producer = KafkaProducer(bootstrap_servers=config["servers"])
        self.topic = settings.LOGGING_KAFKA_TOPIC

    def emit(self, record):
        # drop kafka logging to avoid infinite recursion
        if record.name == "kafka":
            return

        try:
            message = self.formatter.format(record)
            message = message.encode("utf-8")
            self.producer.send(self.topic, message)
        except (KeyboardInterrupt, SystemExit):
            raise
        except Exception:
            self.handleError(record)

    def close(self):
        self.producer.close()
        super().close()


class KafkaFormatter(logging.Formatter):
    # The list contains all the attributes listed in
    # http://docs.python.org/library/logging.html#logrecord-attributes
    skip_list = (
        "args",
        "asctime",
        "created",
        "exc_info",
        "exc_text",
        "filename",
        "funcName",
        "id",
        "levelname",
        "levelno",
        "lineno",
        "module",
        "msecs",
        "msecs",
        "message",
        "msg",
        "name",
        "pathname",
        "process",
        "processName",
        "relativeCreated",
        "thread",
        "threadName",
        "extra",
    )

    easy_types = (str, bool, dict, float, int, list, type(None))

    def __init__(self, schema="logstash", **options):
        self.schema = schema
        self.options = options

        # fully qualified domain name (FQDN)
        if self.options.get("fqdn"):
            self.host = socket.getfqdn()
        else:
            self.host = socket.gethostname()

    def format(self, record):
        message = {
            "logger": record.name,
            "path": record.pathname,
            "level": record.levelname,
            "message": record.getMessage(),
            "service": settings.NAME,
            "schema": self.schema,
            "host": self.host,
        }

        # add logstash info
        if self.schema == "logstach":
            timestamp = datetime.datetime.utcfromtimestamp(record.created).strftime("%Y-%m-%dT%H:%M:%S")
            timestamp += "." + str(timestamp.microsecond / 1000).zfill(3) + "Z"
            message.update({
                "tags": self.options.get("tags", []),
                "@timestamp": timestamp,
                "@version": "1",
            })

        # add extra fields
        message.update(self.get_extra_fields(record))

        # add debug info
        if record.exc_info:
            message.update(self.get_debug_fields(record))

        return json.dumps(message)

    def get_extra_fields(self, record):
        fields = {}

        for key, value in record.__dict__.items():
            if key not in self.skip_list:
                if isinstance(value, self.easy_types):
                    fields[key] = value
                else:
                    fields[key] = repr(value)

        return fields

    def get_debug_fields(self, record):
        return {
            "stack_trace": self.format_exception(record.exc_info),
            "lineno": record.lineno,
            "process": record.process,
            "thread_name": record.threadName,
        }

    def format_exception(self, exc_info):
        exception = ""
        if exc_info:
            exception = "".join(traceback.format_exception(*exc_info))
        return exception


def setup_logging(name, **kwargs):
    logger = logging.getLogger(name=name)
    if logger.handlers:
        return logger

    logger.setLevel(kwargs.get("level", settings.LOGGING_LEVEL))
    logger.propagate = kwargs.get("propagate", settings.LOGGING_PROPAGATE)

    formatter = kwargs.get("formatter", settings.LOGGING_DEFAULT_FORMAT)

    if settings.LOGGING_ENABLE_CONSOLE:
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(LogFormatter(formatter))
        console_handler.setLevel(logging.DEBUG)
        logger.addHandler(console_handler)

    if settings.LOGGING_ENABLE_LOGFILE:
        logfile_handler = RotatingFileHandler(
            filename=os.path.join(get_log_dir(), f"{name}.log"),
            maxBytes=settings.LOGGING_ROTATE_MAX_BYTES,
            backupCount=settings.LOGGING_ROTATE_BACKUP_COUNT,
            encoding="utf8",
        )
        logfile_handler.setFormatter(LogFormatter(formatter))
        logfile_handler.setLevel(logging.DEBUG)
        logger.addHandler(logfile_handler)

    if settings.LOGGING_ENABLE_KAFKA:
        kafka_handler = KafkaLoggingHandler()
        kafka_handler.setFormatter(KafkaFormatter())
        kafka_handler.setLevel(logging.DEBUG)
        logger.addHandler(kafka_handler)

    return logger
