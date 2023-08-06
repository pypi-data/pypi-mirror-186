import json
from dataclasses import dataclass
from typing import Self, Any, Dict

from bot_plugin.domain.access_type import AccessType
from bot_plugin.domain.plugin_context import PluginContext


@dataclass
class PluginRequest:
    url: str
    context: PluginContext
    access_type: AccessType = AccessType.PUBLIC

    def to_json(self) -> str:
        return json.dumps(self, default=lambda o: o.__dict__)

    @staticmethod
    def from_json(json_dict: Dict[str, Any]):
        return {
            'url' in json_dict: lambda: PluginRequest(**json_dict),
            'resource_id' in json_dict: lambda: PluginContext(**json_dict)
        }.get(True, lambda: json_dict)()

