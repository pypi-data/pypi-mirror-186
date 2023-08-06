# coding=utf-8

import threading
from importlib import import_module

from loguru import logger

from applyx.conf import settings
from applyx.utils import check_connection


class RedisManager:

    _mutex = threading.Lock()
    _instance = None

    def __new__(cls, *args, **kwargs):
        with cls._mutex:
            if cls._instance is None:
                cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance

    @classmethod
    def setup(cls):
        cls._instance = cls()

    @classmethod
    def instance(cls):
        return cls._instance

    def __init__(self):
        self.engines = {}

    def get(self, alias):
        return self.engines.get(alias)

    def init_redis(self, alias):
        if alias in self.engines:
            return

        if not hasattr(settings, "REDIS"):
            return

        config = settings.REDIS.get(alias)
        if not config:
            return

        if not config.get("startup_nodes"):
            if not check_connection(config["host"], config["port"]):
                logger.error("redis server {host}:{port} connection refused".format(**config))
                return

            redis = import_module("redis")
            self.engines[alias] = redis.StrictRedis(
                host=config["host"],
                port=config["port"],
                db=config["db"],
                password=config["password"],
                max_connections=config["max_connections"],
                decode_responses=config["decode_responses"],
            )
        else:
            rediscluster = import_module("rediscluster")
            ok = True
            for node in config["startup_nodes"]:
                if not check_connection(node["host"], node["port"]):
                    logger.error("redis server {host}:{port} connection refused".format(**config))
                    ok = False
                    break

            if not ok:
                return

            self.engines[alias] = rediscluster.RedisCluster(
                startup_nodes=config["startup_nodes"],
                max_connections=config["max_connections"],
            )

        logger.info(f"redis [{alias}] ready.")

    def close_redis(self, alias):
        if alias not in self.engines:
            return

        pool = self.engines[alias].connection_pool
        pool.disconnect()

        logger.info(f"redis [{alias}] closed.")

    def init_all_redis(self):
        if not hasattr(settings, "REDIS"):
            return

        for alias in settings.REDIS:
            self.init_redis(alias)

    def close_all_redis(self):
        for alias in self.engines:
            self.close_redis(alias)
