# coding=utf-8

from celery.schedules import crontab

from applyx.celery.base import setup_signals
from applyx.conf import settings
settings.merge_config_module('project.conf.config')

setup_signals()

enable_utc = settings.CELERY_ENABLE_UTC
timezone = settings.CELERY_TIMEZONE
broker_url = settings.CELERY_BROKER_URL
result_backend = settings.CELERY_RESULT_BACKEND
result_expires = settings.CELERY_RESULT_EXPIRES
result_persistent = settings.CELERY_RESULT_PERSISTENT
task_send_sent_event = settings.CELERY_TASK_SEND_SENT_EVENT
worker_hijack_root_logger = settings.CELERY_WORKER_HIJACK_ROOT_LOGGER


imports = [
    "project.celery.tasks.demo",
]

task_routes = {
    "project.celery.tasks.demo": {"queue": "cron"},
}

beat_schedule = {
    "run-demo": {
        "task": "project.celery.tasks.demo",
        "schedule": crontab(hour="*", minute="*/30"),
    },
}
