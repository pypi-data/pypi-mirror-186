import aiohttp as aiohttp

from bot_plugin.consts.routes import AppRoutes
from bot_plugin.domain.plugin_request import PluginRequest


class AppClient:
    def __init__(self, app_url: str):
        self._app_url = app_url

    async def plugin(self, request: PluginRequest):
        async with aiohttp.ClientSession(self._app_url) as session:
            async with session.post(AppRoutes.PLUGIN_MODULE, data=request.to_json()) as response:
                response.raise_for_status()

    async def unplug(self):
        async with aiohttp.ClientSession(self._app_url) as session:
            async with session.post(AppRoutes.UNPLUG_MODULE) as response:
                response.raise_for_status()
