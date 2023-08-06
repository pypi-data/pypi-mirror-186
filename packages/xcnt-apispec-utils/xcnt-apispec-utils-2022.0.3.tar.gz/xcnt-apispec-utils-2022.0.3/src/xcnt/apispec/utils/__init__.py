from typing import List

from apispec.plugin import BasePlugin

from .flask_plugin import get_flask_plugin
from .marshmallow_plugin import get_marshmallow_plugin
from .search_param_plugin import get_search_param_plugin

try:
    from .flasgger_api_spec import FlasggerAPISpec as APISpec  # noqa: F401
except ImportError:
    pass

try:
    from .swagger import get_swagger  # noqa: F401
except ImportError:
    pass


def apispec_plugins() -> List[BasePlugin]:
    return list(
        item
        for item in (
            get_flask_plugin(),
            get_search_param_plugin(),
            get_marshmallow_plugin(),
        )
        if item is not None
    )
