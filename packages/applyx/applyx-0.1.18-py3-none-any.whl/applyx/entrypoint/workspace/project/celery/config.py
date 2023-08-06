# coding=utf-8

from applyx.conf import settings
settings.merge_config_module('project.conf.config')


enable_utc = settings.CELERY_ENABLE_UTC
timezone = settings.CELERY_TIMEZONE
broker_url = settings.CELERY_BROKER_URL
