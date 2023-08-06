# coding=utf-8

import base64
import asyncio
import aiohttp

from loguru import logger
from attrdict import AttrDict

from applyx.conf import settings
from applyx.exception import ServiceException


class BaseService:
    loop = None

    def __init__(self, loop=None):
        self.loop = loop or asyncio.get_event_loop()

    async def rpc(self, method, url, headers={}, timeout=5, **kwargs):
        logger.info(f"[rpc] {method} {url}")

        user_agent = f"{settings.NAME}/{settings.VERSION}"
        headers.update({"User-Agent": user_agent})

        if headers:
            logger.info(f"[rpc] HEADERS {str(headers)}")

        params_data = kwargs.get("params", {})
        if params_data:
            logger.info(f"[rpc] PARAMS {str(params_data)}")

        json_data = kwargs.get("json", {})
        if json_data:
            logger.info(f"[rpc] JSON {str(json_data)}")

        client_timeout = aiohttp.ClientTimeout(total=timeout)
        async with aiohttp.ClientSession(timeout=client_timeout) as session:
            try:
                response = await session.request(method, url, headers=headers, **kwargs)
            except Exception as e:
                logger.error(f"[rpc] {e.__class__.__name__} {str(e)}")
                raise ServiceException("外部服务不可用")

            status = response.status
            reason = response.reason
            if 200 <= status <= 206:
                logger.info(f"[rpc] {status} - {reason}")
                result = await response.json()
                return result

            logger.error(f"[rpc] {status} - {reason}")
            raise ServiceException("外部服务不可用")


class ProxyService(BaseService):
    endpoint = ""

    def __init__(self, endpoint=""):
        super().__init__()
        self.endpoint = endpoint

    async def get(self, path, **kwargs):
        return await self.make_request("GET", path, **kwargs)

    async def post(self, path, **kwargs):
        return await self.make_request("POST", path, **kwargs)

    async def put(self, path, **kwargs):
        return await self.make_request("PUT", path, **kwargs)

    async def delete(self, path, **kwargs):
        return await self.make_request("DELETE", path, **kwargs)

    async def options(self, path, **kwargs):
        return await self.make_request("OPTIONS", path, **kwargs)

    async def head(self, path, **kwargs):
        return await self.make_request("HEAD", path, **kwargs)

    async def make_request(self, method, path, **kwargs):
        url = self.endpoint + path
        result = await self.rpc(method, url, **kwargs)
        return result


class KongService(ProxyService):
    config = None

    def __init__(self, service="", loop=None):
        if not service:
            raise ServiceException("外部服务未指定")

        config = settings.KONG["services"].get(service)
        if not config:
            raise ServiceException("外部服务配置不存在")

        self.config = AttrDict(config)

        gateway = settings.KONG["gateway"]
        endpoint = f"http://{gateway}/{service}/v{self.config.version}"
        super().__init__(endpoint=endpoint)

    async def make_request(self, method, path, **kwargs):
        auth_headers = self.make_auth_headers()
        headers = kwargs.pop("headers", {})
        headers.update(auth_headers)
        return await super().make_request(method, path, headers=headers, **kwargs)

    def make_auth_headers(self):
        origin_auth = f"{self.config.auth.username}:{self.config.auth.password}"
        base64_auth = base64.b64encode(origin_auth.encode("utf8")).decode("utf8")
        return {"Authorization": f"Basic {base64_auth}"}


class NoneResponse:

    # 用于 if 条件判断
    def __eq__(self, other):
        if not other:
            return True
        return False

    def __aenter__(self):
        return self

    def __aexit__(self, exc_type, exc_value, exc_tb):
        return
