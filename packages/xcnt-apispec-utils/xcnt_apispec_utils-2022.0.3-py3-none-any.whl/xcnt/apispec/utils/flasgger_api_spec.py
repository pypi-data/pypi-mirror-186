from contextlib import nullcontext
from typing import Any, Callable, ContextManager, Dict, Iterable, Optional

from apispec.exceptions import DuplicateComponentNameError
from flasgger import APISpec
from flasgger.utils import ordered_dict_to_dict
from flask import Flask


def apispec_to_template(
    app: Optional[Flask],
    spec: APISpec,
    definitions: Optional[Iterable[Any]] = None,
    paths: Optional[Iterable[Any]] = None,
) -> Dict[str, Any]:
    """
    Converts apispec object in to flasgger definitions template
    :param app: Current app
    :param spec: apispec.APISpec
    :param definitions: a list of [Schema, ..] or [('Name', Schema), ..]
    :param paths: A list of flask views
    """
    definitions = definitions or []
    paths = paths or []
    context: Callable[[], ContextManager]
    if app is not None:
        context = app.app_context  # type: ignore[assignment]
    else:
        context = nullcontext

    with context():
        for definition in definitions:
            if isinstance(definition, (tuple, list)):
                name, schema = definition
            else:
                schema = definition
                name = schema.__name__.replace("Schema", "")

            try:
                spec.components.schema(name, schema=schema)
            except DuplicateComponentNameError:
                pass

        for path in paths:
            spec.path(view=path)

    spec_dict = spec.to_dict()
    ret = ordered_dict_to_dict(spec_dict)
    return ret


class FlasggerAPISpec(APISpec):
    def to_flasgger(
        self,
        app: Optional[Flask] = None,
        definitions: Optional[Iterable[Any]] = None,
        paths: Optional[Iterable[Any]] = None,
    ) -> Dict[str, Any]:
        return apispec_to_template(app, self, definitions=definitions, paths=paths)
