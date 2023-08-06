import abc
from aiohttp import web

class BasePluginHandler(abc.ABC):
    async def hanlde(request: web.Request) -> None:
        pass