# coding=utf-8

import sys
import os
from importlib import import_module

import gunicorn
from gunicorn.app.base import BaseApplication
from loguru import logger

from applyx.conf import settings
from applyx.fastapi.builder import FastAPIBuilder
from applyx.utils import get_log_dir


class GunicornApplication(BaseApplication):
    @classmethod
    def get_app(cls, project):
        module_path = f"{project.__package__}.api.gunicorn"
        try:
            module = import_module(module_path)
        except ModuleNotFoundError:
            return cls(project)

        app_cls = getattr(module, "Application", None)
        if app_cls is None or not issubclass(app_cls, cls):
            print(f"invalid flask application path {module_path}:APP")
            return None

        return app_cls(project)

    def __init__(self, project):
        gunicorn.SERVER_SOFTWARE = "Linux"
        self.app = FastAPIBuilder.get_app(project)
        self.project = project
        self.logger = logger
        if self.app is None:
            sys.exit(1)
        super().__init__()

    def init(self, parser, opts, args):
        pass

    def load(self):
        return self.app

    def load_config(self):
        self.cfg.set("on_starting", self.on_starting)
        self.cfg.set("when_ready", self.when_ready)
        self.cfg.set("post_worker_init", self.post_worker_init)
        self.cfg.set("worker_int", self.worker_int)
        self.cfg.set("worker_abort", self.worker_abort)

        try:
            api_config = import_module(f"{self.project.__package__}.conf.config")
        except ModuleNotFoundError as e:
            raise e

        default_config = import_module("applyx.gunicorn.config")
        for setting in dir(default_config):
            if setting.isupper():
                setting_value = getattr(default_config, setting)
                self.cfg.set(setting.lower(), setting_value)

        for setting in dir(api_config):
            if setting.isupper() and setting.startswith("GUNICORN_"):
                setting_value = getattr(api_config, setting)
                self.cfg.set(setting[len("GUNICORN_") :].lower(), setting_value)

    def run(self):
        if self.cfg.daemon:
            gunicorn.util.daemonize(self.cfg.enable_stdio_inheritance)
        super().run()

    def on_starting(self, server):
        self.logger.info("gunicorn is starting")
        os.makedirs(get_log_dir(), exist_ok=True)

    def when_ready(self, server):
        self.logger.info("gunicorn is ready")

    def post_worker_init(self, worker):
        self.logger.info("gunicorn worker inited")

    def worker_int(self, worker):
        pass

    def worker_abort(self, worker):
        pass
