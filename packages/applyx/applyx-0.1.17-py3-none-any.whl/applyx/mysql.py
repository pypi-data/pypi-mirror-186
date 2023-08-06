# coding=utf-8

import threading

from loguru import logger
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base

from applyx.conf import settings
from applyx.utils import check_connection


Base = declarative_base()


class MySQLManager:

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

    def init_all_mysql(self):
        if not hasattr(settings, "MYSQL"):
            return

        for key in settings.MYSQL:
            config = settings.MYSQL[key]

            if not check_connection(config["host"], config["port"]):
                logger.error("mysql server {host}:{port} connection refused".format(**config))
                continue

            connection_string = (
                "mysql+pymysql://{username}:{password}@{host}:{port}/{database}".format(
                    **config
                )
            )
            engine = sqlalchemy.create_engine(
                connection_string,
                echo=True,
                max_overflow=0,
                pool_size=config["pool_size"],
                pool_timeout=config["pool_timeout"],
                pool_recycle=config["pool_recycle"],
            )
            self.engines[key] = engine
            # from sqlalchemy.orm import sessionmaker
            # session_cls = sessionmaker(bind=engine)
            # session = session_cls()

            logger.info(f"mysql [{key}] ready.")

    def close_all_mysql(self):
        if not hasattr(settings, "MYSQL"):
            return

        for key in settings.MYSQL:
            engine = self.engines[key]
            engine.dispose()

            logger.info(f"mysql [{key}] closed.")
