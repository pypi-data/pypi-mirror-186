# coding=utf-8

import sys
import os
import json
import logging
import argparse
import traceback
from importlib import import_module
from logging.handlers import RotatingFileHandler

from loguru import logger

from applyx.conf import settings
from applyx.utils import check_connection, get_log_dir


class BaseScript:
    def __init__(self, variables={}, debug=False, **kwargs):
        self.variables = variables
        self.debug = debug

    def init_logger(self):
        _, _, name = self.__class__.__module__.split(".")
        sink = RotatingFileHandler(
            filename=os.path.join(get_log_dir(), f"scripts.{name}.log"),
            maxBytes=settings.LOGGING_ROTATE_MAX_BYTES,
            backupCount=settings.LOGGING_ROTATE_BACKUP_COUNT,
            encoding="utf8",
        )
        logging_level = logging.DEBUG if self.debug else settings.LOGGING_LEVEL
        logging_format = self.get_logging_format()

        logger.remove()
        logger.add(sink=sys.stderr, level=logging_level, format=logging_format)
        logger.add(sink=sink, level=logging_level, format=logging_format)

    def get_logging_format(self):
        return settings.LOGGING_DEFAULT_FORMAT

    def run(self):
        raise NotImplementedError


class KafkaScript(BaseScript):
    topic = ""
    group_id = None
    message = None
    consumer = None

    def get_logging_format(self):
        logging_format = (
            "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | "
            "<level>{level}</level> | "
            "<cyan>({process},{thread})</cyan> "
            "[{extra[offset]}] - {message}"
        )
        logger.configure(extra={"offset": "x"})
        return logging_format

    def run(self):
        config = getattr(settings, "KAFKA", None)
        if config is None:
            raise Exception("missing settings for KAFKA")

        for server in config["servers"]:
            host, port = server.split(":")
            if not check_connection(host, int(port)):
                logger.error(f"kafka server {host}:{port} connection refused")
                sys.exit(0)

        kafka = import_module("kafka")
        self.consumer = kafka.KafkaConsumer(
            self.topic,
            group_id=self.group_id,
            bootstrap_servers=config["servers"],
            auto_offset_reset="latest",
            value_deserializer=json.loads,
        )

        logger.info(f"listening on {self.topic}")

        try:
            for message in self.consumer:
                self.message = message
                logger.info(f"[payload] {message.value}")
                with logger.contextualize(offset=message.offset):
                    self.on_message()
        except Exception:
            logger.error(traceback.format_exc())

    def on_message(self):
        raise NotImplementedError


class BaseCommand:
    def __init__(self, project):
        self.project = project

    def register(self, subparser):
        raise NotImplementedError

    def invoke(self, args):
        raise NotImplementedError


class Manager:
    def __init__(self):
        # import stat
        # os.umask(stat.S_IRXWG | stat.S_IRWXO) # set umask to 0o077
        os.makedirs(get_log_dir(), exist_ok=True)

        logger._core.handlers.pop(0)
        logger.add(sys.stderr, format=settings.LOGURU_DEFAULT_FORMAT)

    def run(self, project):
        settings.merge_config_module(project.config)

        parser = argparse.ArgumentParser(description=f"help for {settings.NAME} entrypoint")
        parser.add_argument("--version", action="version", version=settings.VERSION)
        subparser = parser.add_subparsers(dest="cmd")
        cmd_module_names = ["flask", "fastapi", "gunicorn", "script", "shell", "clean"]
        commands = {}
        for cmd in cmd_module_names:
            cmd_module = import_module(f"applyx.command.{cmd}")
            cmd_class = getattr(cmd_module, "Command", None)
            cmd_instance = cmd_class(project)
            cmd_instance.register(subparser)
            commands[cmd] = cmd_instance

        argv = sys.argv[1:] if len(sys.argv[1:]) else ["-h"]
        args = parser.parse_args(argv)
        cmd = args.__dict__.pop("cmd")

        config = import_module(f"{project.__package__}.conf.config")

        try:
            commands[cmd].invoke(args)
        except KeyboardInterrupt:
            sys.exit(0)
