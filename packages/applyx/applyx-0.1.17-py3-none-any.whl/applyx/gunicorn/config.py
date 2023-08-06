# coding=utf-8

import os
from applyx.conf import settings

# http://docs.gunicorn.org/en/latest/settings.html

# Server Socket
BIND = "0.0.0.0:8888"
BACKLOG = 1024 * 2

# Worker Processes
WORKERS = os.cpu_count() * 2 + 1
# WORKER_CLASS = 'gevent'
WORKER_CLASS = "uvicorn.workers.UvicornH11Worker"
WORKER_CONNECTIONS = 1000
MAX_REQUESTS = 0
TIMEOUT = 60 * 5  # in seconds
GRACEFUL_TIMEOUT = 10  # in seconds
KEEPALIVE = 2  # in seconds

# Security
LIMIT_REQUEST_LINE = 1024 * 4
LIMIT_REQUEST_FIELDS = 100
LIMIT_REQUEST_FIELD_SIZE = 1024 * 8

# Logging
LOGLEVEL = "info"
DISABLE_REDIRECT_ACCESS_TO_SYSLOG = True
ACCESSLOG = "gunicorn.access.log"
ERRORLOG = "gunicorn.error.log"
