from typing import Optional

from apispec.plugin import BasePlugin

try:
    from apispec_webframeworks.flask import FlaskPlugin

    def get_flask_plugin() -> Optional[BasePlugin]:
        return FlaskPlugin()


except ImportError:

    def get_flask_plugin() -> Optional[BasePlugin]:
        return None
