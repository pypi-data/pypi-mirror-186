from __future__ import annotations

from typing import Any, Dict, Optional

from apispec.plugin import BasePlugin
from marshmallow.exceptions import RegistryError

try:
    import marshmallow_enum
except ImportError:
    marshmallow_enum = None
from apispec.ext.marshmallow import MarshmallowPlugin as _MarshmallowPlugin
from apispec.ext.marshmallow.openapi import OpenAPIConverter as _OpenAPIConverter
from marshmallow.fields import Field


def enum_to_properties(self: OpenAPIConverter, field: Field, **kwargs: Dict[str, Any]) -> Dict[Any, Any]:
    assert marshmallow_enum is not None
    if isinstance(field, marshmallow_enum.EnumField):
        return {"type": "string", "enum": [m.name for m in field.enum]}
    return {}


class OpenAPIConverter(_OpenAPIConverter):
    def __init__(self, openapi_version: str, schema_name_resolver: Any, spec: Any) -> None:
        super().__init__(openapi_version, schema_name_resolver, spec)
        if marshmallow_enum is not None:
            self.add_attribute_function(enum_to_properties)


class MarshmallowPlugin(_MarshmallowPlugin):
    Converter = OpenAPIConverter

    def schema_helper(self, name: str, definition: Any, schema: Optional[Any] = None, **kwargs: Any) -> Any:
        try:
            return super().schema_helper(name, definition, schema, **kwargs)
        except RegistryError:
            return None


def get_marshmallow_plugin() -> Optional[BasePlugin]:
    plugin = MarshmallowPlugin()
    return plugin
