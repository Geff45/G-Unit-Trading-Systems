"""
Query Registry.
"""

from __future__ import annotations

from typing import Any, Dict, Type

from .query import Query
from .query_handler import QueryHandler


class QueryRegistry:
    """
    Stores query handlers.
    """

    def __init__(self) -> None:
        self._handlers: Dict[
            Type[Query],
            QueryHandler[Any, Any],
        ] = {}

    def register(
        self,
        query_type: Type[Query],
        handler: QueryHandler[Any, Any],
    ) -> None:
        """
        Register a handler.
        """

        self._handlers[query_type] = handler

    def contains(
        self,
        query_type: Type[Query],
    ) -> bool:
        return query_type in self._handlers

    def resolve(
        self,
        query_type: Type[Query],
    ) -> QueryHandler[Any, Any]:
        return self._handlers[query_type]