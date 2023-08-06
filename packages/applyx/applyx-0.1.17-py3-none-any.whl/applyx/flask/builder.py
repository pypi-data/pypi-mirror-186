# coding=utf-8

import os
import logging
import traceback
from importlib import import_module
from logging.handlers import RotatingFileHandler

import shortuuid
from attrdict import AttrDict
from flask import Flask
from flask import request
from flask import jsonify
from flask import Response
from flask import abort
from flask import has_request_context
from flask_compress import Compress
from werkzeug.routing import BaseConverter
from werkzeug.exceptions import HTTPException
from werkzeug.serving import WSGIRequestHandler
from jinja2 import FileSystemLoader

from applyx.conf import settings
from applyx.exception import ServiceException
from applyx.flask.views import ViewWrapper
from applyx.jinja2 import FILTERS, TESTS
from applyx.utils import get_log_dir


class RegexConverter(BaseConverter):
    def __init__(self, url_map, *args):
        super().__init__(url_map)
        self.regex = args[0]


class RequestHandler(WSGIRequestHandler):
    def log(self, type, message, *args):
        content = "%s [%s] %s" % (
            self.address_string(),
            self.log_date_time_string(),
            message % args,
        )
        logger = logging.getLogger("werkzeug")
        getattr(logger, type)(content)


class FlaskBuilder:
    @classmethod
    def get_app(cls, project, debug=False):
        module_path = f"{project.__package__}.api.flask"
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
        self.uuid = shortuuid.ShortUUID(alphabet="0123456789ABCDEF")

    def make(self, **kwargs):
        self.init_config()
        self.init_logging()

        flask_kwargs = {}
        if getattr(self.config, "STATIC_DIR", ""):
            path = os.path.realpath(self.config.STATIC_DIR)
            if not os.path.exists(path):
                raise Exception(f"static path {path} not exists")
            flask_kwargs.update({"static_folder": path, "static_url_path": "/static"})

        self.app = Flask(settings.NAME, **flask_kwargs)
        self.app.config.from_mapping(dict(self.config.items()))

        if kwargs.get("enable_gzip", True):
            compress = Compress()
            compress.init_app(self.app)

        self.app.url_map.converters["regex"] = RegexConverter

        self.setup_routes()
        self.setup_session()
        self.setup_jinja2()

        self.app.before_first_request(self.hook_before_first_request)
        self.app.before_request(self.hook_before_request)
        self.app.after_request(self.hook_after_request)
        self.app.register_error_handler(Exception, self.hook_handle_exception)
        # self.app.do_teardown_appcontext(self.hook_do_teardown_appcontext)

        if self.debug:
            logger.warning("Debug mode is on.")

        return self.app

    def init_config(self):
        try:
            api_config = import_module(f"{self.project.__package__}.conf.config")
        except ModuleNotFoundError as e:
            raise e

        default_config = import_module("applyx.flask.config")
        for setting in dir(default_config):
            if setting.isupper():
                setting_value = getattr(default_config, setting)
                setattr(self.config, setting, setting_value)

        prefix = "FLASK_"
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

        self.app.jinja_loader = FileSystemLoader(path)
        env = self.app.jinja_env
        env.filters.update(FILTERS)
        env.tests.update(TESTS)
        env.globals.update({"WEB": self.config.WEB})

    def setup_routes(self):
        base_path = os.path.join(self.api_dir, "views")
        for dirpath, _, filenames in os.walk(base_path):
            for filename in filenames:
                full_pathname = os.path.join(dirpath, filename)
                if filename.startswith("_") or not filename.endswith(".py"):
                    continue
                package_dir = os.path.abspath(os.path.join(self.project.__path__[0], os.pardir))
                module_path = full_pathname[len(package_dir) + 1: -len(".py")].replace(os.sep, ".")
                module = import_module(module_path)
                for key in dir(module):
                    if key.startswith("_"):
                        continue
                    value = getattr(module, key)
                    if not isinstance(value, ViewWrapper):
                        continue
                    relative_path = full_pathname[len(base_path) + 1 : -len(".py")].replace(os.sep, ".")
                    name = f"views.{relative_path}.{key}"
                    view_func = value(name)
                    self.app.add_url_rule(value.route, view_func=view_func)

    def get_remote_address(self):
        environ = request.environ
        remote_host, remote_port = environ["REMOTE_ADDR"], environ["REMOTE_PORT"]
        # local_host, local_port = environ['SERVER_NAME'], environ['SERVER_PORT']

        if request.headers.get("X-Forwarded-For"):
            # HTTP_X_FORWARDED_FOR can be a comma-separated list of IPs.
            # Take just the first one.
            x_forwarded_for = request.headers["X-Forwarded-For"]
            ips = [item.strip() for item in x_forwarded_for.split(",")]
            remote_host = ips.pop(0)
        elif request.headers.get("Remote-Addr"):
            remote_host = request.headers["Remote-Addr"]
        elif request.headers.get("X-Real-IP"):
            remote_host = request.headers["X-Real-IP"]

        if request.headers.get("Remote-Port"):
            remote_port = int(request.headers["Remote-Port"])

        return remote_host, remote_port

    def validate_crossdomain_request(self):
        if not self.config.ENABLE_CORS:
            return False
        return True
        # return request.headers.get('Origin', '').endswith(self.config.CORS_WHITELIST_DOMAINS)

    def hook_before_first_request(self):
        pass

    def hook_before_request(self):
        request.id = self.uuid.random(length=4)
        if request.path.startswith("/static"):
            return

        with logger.contextualize(mdc=request.state.id):
            logger.info(f"[uri] {request.method} {request.path}")

            if request.endpoint is not None:
                logger.info(f"[view] {request.endpoint}")

            headers = dict(request.headers)
            if headers:
                logger.debug(f"[headers] {str(headers)}")

            query = request.args.to_dict()
            if query:
                logger.info(f"[query] {str(query)}")

            form = request.form.to_dict()
            if form:
                logger.info(f"[form] {str(form)}")

            if request.data:
                data = request.get_json(silent=True) if request.is_json else request.data.decode("utf8")
                logger.info(f"[data] {str(data)}")

            files = request.files.to_dict()
            if files:
                logger.info(f"[files] {str(files)}")

        if request.method == "OPTIONS" and "Access-Control-Request-Method" in request.headers:
            if not self.validate_crossdomain_request():
                return abort(404)

            headers = {
                "CONTENT-TYPE": "text/html",
                "Access-Control-Max-Age": str(self.config.ACCESS_CONTROL_MAX_AGE),
                "Access-Control-Allow-Origin": request.headers.get("Origin", ""),
                "Access-Control-Allow-Methods": request.headers["Access-Control-Request-Method"],
                "Access-Control-Allow-Headers": request.headers.get("Access-Control-Request-Headers", ""),
                # 'Access-Control-Allow-Credentials': 'true',
            }
            return Response(status=200, headers=headers)

    def hook_after_request(self, response):
        if request.path.startswith("/static"):
            if request.path.endswith(".ejs"):
                response.headers["Content-Type"] = "text/html; charset=utf-8"
            return response

        response.headers["X-Request-Id"] = request.id

        with logger.contextualize(mdc=request.state.id):
            logger.info(f"[http] {response.status_code}")
            if response.is_json:
                logger.info(f"[err] {response.json['err']}")

                if response.json.get("msg"):
                    logger.info(f"[msg] {response.json['msg']}")

                if response.json.get("log"):
                    logger.info(f"[log] {response.json['log']}")

        return response

    def hook_handle_exception(self, error):
        if isinstance(error, HTTPException):
            return error.name, error.code

        if isinstance(error, ServiceException):
            return jsonify(err=1, msg=error.msg)

        # generic 500 Internal Server Error
        content = "Internal Server Error"
        logger.exception(content, exc_info=error)

        if self.debug:
            content = traceback.format_exc()

        return Response(content, status=500)

    def hook_do_teardown_appcontext(self):
        pass

    def setup_session(self):
        if not hasattr(self.config, "SESSION_TYPE"):
            return

        # https://pythonhosted.org/Flask-Session/
        if self.config.SESSION_TYPE != "redis":
            # TODO: adapt for memcache / filesystem / mongodb / sqlalchemy
            logger.error(f"unsupported session type {self.config.SESSION_TYPE}")
            return

        if not hasattr(settings, "REDIS") or "session" not in settings.REDIS:
            return

        import flask_session
        from applyx.redis import RedisManager

        session_redis = RedisManager.instance().get(self.config.SESSION_REDIS_ALIAS)
        if session_redis:
            self.config.SESSION_REDIS = session_redis
            flask_session.Session().init_app(self.app)
