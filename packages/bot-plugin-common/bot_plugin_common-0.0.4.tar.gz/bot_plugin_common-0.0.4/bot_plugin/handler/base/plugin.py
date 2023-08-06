import abc

from aiohttp import web


class BasePluginHandler(abc.ABC):
    async def handle_message_event(self, request: web.Request) -> None:
        pass

    async def handle_callback_query_event(self, request: web.Request) -> None:
        pass



