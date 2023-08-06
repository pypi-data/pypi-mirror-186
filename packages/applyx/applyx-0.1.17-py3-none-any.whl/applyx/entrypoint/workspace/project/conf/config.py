# coding=utf-8

import os

NAME = "PROJECT"
VERSION = "1.0"

WORKSPACE = os.path.realpath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir))

REDIS = {
    "default": {
        "host": "127.0.0.1",
        "port": 6379,
        "db": 1,
        "password": None,
        "max_connections": 10,
        "decode_responses": True,
    },
}

# MONGODB = {
#     'default': {
#         'host': '127.0.0.1',
#         'port': 27017,
#         'db': 'database_name',
#         'username': None,
#         'password': None,
#         'maxpoolsize': 10,
#         'connect': False,
#     },
# }

WEB = {
    "env": "local",
    "ssl": False,
    "static": "/static/",
    "cdn": "/static/vendor/",
    "cache": "1.0.0",
}

FASTAPI_DEBUG = True
FASTAPI_ENABLE_GZIP = True
FASTAPI_ENABLE_CORS = True
FASTAPI_CORS_WHITELIST_DOMAINS = ["*"]
FASTAPI_ENABLE_SESSION = False
FASTAPI_SESSION_KEY_PREFIX = "session:"
FASTAPI_SESSION_REDIS_ALIAS = "default"
FASTAPI_STATIC_DIR = os.path.join(WORKSPACE, 'project/static')

GUNICORN_BIND = "0.0.0.0:8888"
GUNICORN_WORKERS = 1

CELERY_BROKER_URL = "redis://{host}:{port}/{db}".format(**REDIS["default"])
