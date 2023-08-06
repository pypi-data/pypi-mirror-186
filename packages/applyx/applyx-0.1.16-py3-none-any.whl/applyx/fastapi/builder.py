# coding=utf-8

import sys
import os
import logging
from importlib import import_module
from logging.handlers import RotatingFileHandler

from celery import Celery
from loguru import logger
from attrdict import AttrDict
from starlette.requests import Request
from starlette.exceptions import HTTPException
from starlette.middleware.gzip import GZipMiddleware
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
from uvicorn.middleware.proxy_headers import ProxyHeadersMiddleware
from fastapi import FastAPI, APIRouter, status
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from applyx.conf import settings
from applyx.exception import ServiceException
from applyx.jinja2 import FILTERS, TESTS
from applyx.fastapi.middlewares import RequestMiddleware, RedisSessionMiddleware
from applyx.utils import get_log_dir


class FastAPIBuilder:
    @classmethod
    def get_app(cls, project, debug=False):
        module_path = f"{project.__package__}.api.fastapi"
        try:
            module = import_module(module_path)
        except ModuleNotFoundError:
            builder_cls = cls
        else:
            builder_cls = getattr(module, "Builder", None)
            if builder_cls is None or not issubclass(builder_cls, cls):
                print(f"invalid flask build path {module_path}.Builder")
                return None

        builder = builder_cls(project, debug)
        builder.make()
        return builder.app

    def __init__(self, project=None, debug=False):
        self.project = project
        self.debug = debug
        self.api_dir = os.path.join(project.__path__[0], "api")
        self.config = AttrDict()
        self.app = None

    def make(self):
        self.init_config()
        self.init_logging()

        fastapi_kwargs = dict(debug=self.debug)
        if self.debug:
            fastapi_kwargs.update(
                openapi_url=self.config.OPENAPI_URL,
                docs_url=self.config.DOCS_URL,
                redoc_url=self.config.REDOC_URL,
            )
        else:
            fastapi_kwargs.update(openapi_url=None, docs_url=None, redoc_url=None)

        self.app = FastAPI(title=settings.NAME, **fastapi_kwargs)
        self.app.globals = AttrDict()

        if getattr(self.config, "STATIC_DIR", ""):
            path = os.path.realpath(self.config.STATIC_DIR)
            if not os.path.exists(path):
                raise Exception(f"static path {path} not exists")
            self.app.mount("/static", StaticFiles(directory=path), name="static")

        self.setup_jinja2()
        self.setup_exception_handlers()
        self.setup_event_handlers()
        self.setup_middlewares()
        self.setup_routes()

        if self.debug:
            logger.warning("Debug mode is on.")

    def init_config(self):
        try:
            api_config = import_module(f"{self.project.__package__}.conf.config")
        except ModuleNotFoundError as e:
            raise e

        default_config = import_module("applyx.fastapi.config")
        for setting in dir(default_config):
            if setting.isupper():
                setting_value = getattr(default_config, setting)
                setattr(self.config, setting, setting_value)

        prefix = "FASTAPI_"
        for setting in dir(api_config):
            if setting.isupper() and setting.startswith(prefix):
                setting_value = getattr(api_config, setting)
                setattr(self.config, setting[len(prefix) :], setting_value)

        if hasattr(api_config, "WEB"):
            setattr(self.config, "WEB", AttrDict(api_config.WEB))

    def init_logging(self):
        sink = RotatingFileHandler(
            filename=os.path.join(get_log_dir(), "web.log"),
            maxBytes=settings.LOGGING_ROTATE_MAX_BYTES,
            backupCount=settings.LOGGING_ROTATE_BACKUP_COUNT,
            encoding="utf8",
        )
        logging_level = logging.DEBUG if self.debug else settings.LOGGING_LEVEL
        logging_format = (
            "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | "
            "<level>{level}</level> | "
            "<cyan>({process},{thread})</cyan> "
            "[{extra[mdc]}] - {message}"
        )

        logger.remove()
        logger.configure(extra={"mdc": "x"})
        logger.add(sink=sys.stderr, level=logging_level, format=logging_format)
        logger.add(sink=sink, level=logging_level, format=logging_format)

    def setup_jinja2(self):
        path = os.path.join(self.api_dir, self.config.TEMPLATE_FOLDER)
        if not os.path.exists(path):
            return

        self.app.jinja_templates = Jinja2Templates(directory=path)
        env = self.app.jinja_templates.env
        env.filters.update(FILTERS)
        env.tests.update(TESTS)
        env.globals.update({"WEB": self.config.WEB})

    def setup_middlewares(self):
        if self.config.ENABLE_GZIP:
            self.app.add_middleware(GZipMiddleware, minimum_size=1000)

        if self.config.ENABLE_CORS:
            self.app.add_middleware(
                CORSMiddleware,
                max_age=self.config.ACCESS_CONTROL_MAX_AGE,
                allow_origins=self.config.CORS_WHITELIST_DOMAINS,
                allow_credentials=True,
                allow_methods=["*"],
                allow_headers=["*"],
            )

        if self.config.ENABLE_SESSION:
            if getattr(settings, "REDIS", None) and self.config.SESSION_REDIS_ALIAS in settings.REDIS:
                self.app.add_middleware(RedisSessionMiddleware, config=self.config)
            else:
                self.app.add_middleware(SessionMiddleware, secret_key=self.config.SESSION_SECRET_KEY)

        self.app.add_middleware(ProxyHeadersMiddleware, trusted_hosts=["*"])
        self.app.add_middleware(RequestMiddleware, config=self.config)

    def setup_exception_handlers(self):
        self.app.add_exception_handler(Exception, self.wrap_handler(self.generic_exception_handler))
        self.app.add_exception_handler(ServiceException, self.wrap_handler(self.generic_exception_handler))
        self.app.add_exception_handler(RequestValidationError, self.wrap_handler(self.request_validation_error_handler))
        self.app.add_exception_handler(HTTPException, self.wrap_handler(self.http_exception_handler))

    def wrap_handler(self, func):
        def wrapped_func(request, exec):
            if request.url.path.startswith("/static"):
                response = func(request, exec)
                return response

            endpoint = request.scope.get("endpoint")
            if endpoint:
                logger.error(f"[endpoint] {endpoint.__module__}.{endpoint.__name__}")

            response = func(request, exec)
            response.headers["X-Request-Id"] = request.state.id
            return response

        return wrapped_func

    def generic_exception_handler(self, request: Request, exc: Exception):
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content=dict(err=1, msg=str(exc)),
        )

    def request_validation_error_handler(self, request: Request, exc: RequestValidationError):
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content=dict(err=1, msg="Request Validation Error.", data=jsonable_encoder(exc.errors())),
        )

    def http_exception_handler(self, request: Request, exc: HTTPException):
        return HTMLResponse(status_code=exc.status_code, content=f"{exc.status_code} - {exc.detail}")

    def setup_event_handlers(self):
        self.app.add_event_handler("startup", self.setup_startup)
        self.app.add_event_handler("shutdown", self.setup_shutdown)

    def setup_startup(self):
        logger.info("Resource init.")

        from applyx.redis import RedisManager
        RedisManager.setup()
        RedisManager.instance().init_all_redis()

        from applyx.mongo import MongoManager
        MongoManager.setup()
        MongoManager.instance().init_all_mongo()

        from applyx.mysql import MySQLManager
        MySQLManager.setup()
        MySQLManager.instance().init_all_mysql()

        logger.info("Resource ready.")

        if settings.CELERY_BROKER_URL:
            self.app.celery = Celery()
            try:
                config = import_module(f"{self.project.__package__}.conf.celery.config")
                self.app.celery.config_from_object(config)
            except Exception as e:
                logger.exception("celery init error", exc_info=e)

        self.on_startup()

    def setup_shutdown(self):
        from applyx.redis import RedisManager

        RedisManager.instance().close_all_redis()

        from applyx.mongo import MongoManager

        MongoManager.instance().close_all_mongo()

        from applyx.mysql import MySQLManager

        MySQLManager.instance().close_all_mysql()

        self.on_shutdown()

    def on_startup(self):
        pass

    def on_shutdown(self):
        pass

    def setup_routes(self):
        base_path = os.path.join(self.api_dir, "routes")
        for filename in os.listdir(base_path):
            full_pathname = os.path.join(base_path, filename)
            if not filename.endswith(".py") or not os.path.isfile(full_pathname):
                continue
            package_dir = os.path.abspath(os.path.join(self.project.__path__[0], os.pardir))
            module_path = full_pathname[len(package_dir) + 1: -len(".py")].replace(os.sep, ".")
            module = import_module(module_path)
            router = getattr(module, "router", None)
            if router and isinstance(router, APIRouter):
                self.app.include_router(router)
