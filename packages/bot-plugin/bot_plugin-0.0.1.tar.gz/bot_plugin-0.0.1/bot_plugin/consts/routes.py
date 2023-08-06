from typing import Final


class Module:
    _BASE: Final[str] = '/module'
    PLUGIN: Final[str] = _BASE + '/plugin'
    UNPLUG: Final[str] = _BASE + '/unplug'
