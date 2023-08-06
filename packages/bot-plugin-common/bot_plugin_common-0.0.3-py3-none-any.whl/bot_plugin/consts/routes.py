from typing import Final


class AppRoutes:
    _MODULE: Final[str] = '/module'
    PLUGIN_MODULE: Final[str] = _MODULE + '/plugin'
    UNPLUG_MODULE: Final[str] = _MODULE + '/unplug'
