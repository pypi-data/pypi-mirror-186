import json
from dataclasses import dataclass

from bot_plugin.domain.access_type import AccessType
from bot_plugin.domain.plugin_context import PluginContext


@dataclass
class PluginRequest:
    url: str
    context: PluginContext
    access_type: AccessType = AccessType.PUBLIC

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)
