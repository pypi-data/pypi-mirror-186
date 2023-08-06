from typing import Optional

from apispec.plugin import BasePlugin

try:
    from .marshmallow_plugin import get_marshmallow_plugin
except ImportError:

    def get_marshmallow_plugin() -> Optional[BasePlugin]:
        return None
