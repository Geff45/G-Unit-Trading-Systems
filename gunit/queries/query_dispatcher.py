"""
Query Dispatcher.
"""

from __future__ import annotations

from typing import Any

from .query import Query
from .query_registry import QueryRegistry


class QueryDispatcher:
    """
    Dispatches queries to their handlers.
    """

    def __init__(
        self,
        registry: QueryRegistry,
    ) -> None:

        self._registry = registry

    @property
    def registry(self) -> QueryRegistry:
        return self._registry

    def dispatch(
        self,
        query: Query,
    ) -> Any:
        """
        Dispatch a query.
        """

        handler = self._registry.resolve(
            type(query)
        )

        return handler.handle(query)