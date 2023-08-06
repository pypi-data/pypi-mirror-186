# coding=utf-8

import os
import logging


##############################
# Basic Configuration
##############################
NAME = "project"
VERSION = "1.0"
DEBUG = False
TIME_ZONE = "Asia/Shanghai"

WORKSPACE = os.getcwd()
LOG_FOLDER = "log"
STORE_FOLDER = "store"

##############################
# Logging Configuration
##############################
LOGGING_LEVEL = logging.INFO
LOGGING_DEFAULT_FORMAT = "%(asctime)s | %(levelname)s | (%(process)d:%(thread)d) - %(message)s"
LOGGING_PROPAGATE = False
LOGGING_ENABLE_CONSOLE = True
LOGGING_ENABLE_LOGFILE = True
LOGGING_ENABLE_KAFKA = False
LOGGING_ROTATE_MAX_BYTES = 1024 * 1024 * 100
LOGGING_ROTATE_BACKUP_COUNT = 10
LOGGING_KAFKA_TOPIC = "kafka_logging"

LOGURU_DEFAULT_FORMAT = (
    "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{level}</level> | "
    "<cyan>({process},{thread})</cyan> - {message}"
)

##############################
# Storage Configuration
##############################
STORAGE_CLASS = "applyx.storage.LocalStorage"
STORAGE_PREFIX = "http://127.0.0.1:8000/"

##############################
# Celery Configuration
##############################
CELERY_ENABLE_UTC = False
CELERY_TIMEZONE = TIME_ZONE
CELERY_RESULT_BACKEND = None
CELERY_RESULT_EXPIRES = 0
CELERY_RESULT_PERSISTENT = False
CELERY_TASK_SEND_SENT_EVENT = True
CELERY_WORKER_HIJACK_ROOT_LOGGER = True
CELERY_BROKER_URL = None
