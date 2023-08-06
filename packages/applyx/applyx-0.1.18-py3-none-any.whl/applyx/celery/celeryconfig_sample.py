# coding=utf-8

from celery.schedules import crontab

from applyx.conf import settings

# from applyx.celery.base import setup_signals
# setup_signals()


enable_utc = settings.CELERY_ENABLE_UTC
timezone = settings.CELERY_TIMEZONE
broker_url = settings.CELERY_BROKER_URL
result_backend = settings.CELERY_RESULT_BACKEND
result_expires = settings.CELERY_RESULT_EXPIRES
result_persistent = settings.CELERY_RESULT_PERSISTENT

worker_hijack_root_logger = settings.CELERY_WORKER_HIJACK_ROOT_LOGGER
worker_log_format = settings.CELERY_WORKER_LOG_FORMAT
worker_task_log_format = settings.CELERY_WORKER_TASK_LOG_FORMAT


imports = [
    "project.tasks.hello",
    "project.tasks.world",
]

task_routes = {
    "project.tasks.hello": {"queue": "async"},
    "project.tasks.world": {"queue": "cron"},
}

beat_schedule = {
    "world": {
        "task": "project.tasks.world",
        "schedule": crontab(minute="*"),
    },
}
