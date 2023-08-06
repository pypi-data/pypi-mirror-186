# coding=utf-8

import threading
import asyncio
from importlib import import_module

from loguru import logger

from applyx.conf import settings
from applyx.aio.utils import check_connection


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

    async def init_redis(self, alias, loop=None):
        if alias in self.engines:
            return

        if not loop:
            loop = asyncio.get_event_loop()

        if not hasattr(settings, "REDIS"):
            return

        config = settings.REDIS.get(alias)
        if not config:
            return

        aredis = import_module("aredis")

        if config.get("startup_nodes"):
            self.engines[alias] = aredis.StrictRedisCluster(
                startup_nodes=config["startup_nodes"],
                max_connections=config["max_connections"],
                decode_responses=config["decode_responses"],
            )
        else:
            ok = await check_connection(config["host"], config["port"], loop)
            if not ok:
                logger.error("redis server {host}:{port} connection refused".format(**config))
                return

            self.engines[alias] = aredis.StrictRedis(
                host=config["host"],
                port=config["port"],
                db=config["db"],
                password=config["password"],
                max_connections=config["max_connections"],
                decode_responses=config["decode_responses"],
            )

        logger.info(f"init redis [{alias}] done ...")

    async def close_redis(self, alias, loop=None):
        if alias not in self.engines:
            return

        if not loop:
            loop = asyncio.get_event_loop()

        pool = self.engines[alias].connection_pool
        pool.disconnect()

        logger.info(f"close redis [{alias}] done ...")

    async def init_all_redis(self, loop=None):
        if not hasattr(settings, "REDIS"):
            return

        for alias in settings.REDIS:
            await self.init_redis(alias, loop)

    async def close_all_redis(self, loop=None):
        for alias in self.engines:
            await self.close_redis(alias, loop)
