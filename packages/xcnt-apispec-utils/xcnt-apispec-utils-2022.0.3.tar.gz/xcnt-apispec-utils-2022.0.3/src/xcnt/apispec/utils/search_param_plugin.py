from typing import Any, Optional

try:
    from xcnt.sqlalchemy.search.apispec import SearchParamPlugin

    def get_search_param_plugin() -> Optional[Any]:
        return SearchParamPlugin()


except ImportError:

    def get_search_param_plugin() -> Optional[Any]:
        return None
