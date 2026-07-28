"""
Query Builder.
"""

from __future__ import annotations

from typing import Any, Type

from .query import Query
from .query_handler import QueryHandler
from .query_registry import QueryRegistry


class QueryBuilder:
    """
    Fluent builder for query registration.
    """

    def __init__(self) -> None:

        self._registry = QueryRegistry()

    @property
    def registry(self) -> QueryRegistry:
        return self._registry

    def add(
        self,
        query_type: Type[Query],
        handler: QueryHandler[Any, Any],
    ) -> "QueryBuilder":
        """
        Register a query handler.
        """

        self._registry.register(
            query_type,
            handler,
        )

        return self

    def build(self) -> QueryRegistry:
        """
        Build the registry.
        """

        return self._registry