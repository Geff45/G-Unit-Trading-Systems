"""
Base Query Handler.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from .query import Query

TQuery = TypeVar("TQuery", bound=Query)
TResult = TypeVar("TResult")


class QueryHandler(ABC, Generic[TQuery, TResult]):
    """
    Handles a query and returns a result.
    """

    @abstractmethod
    def handle(
        self,
        query: TQuery,
    ) -> TResult:
        """
        Handle the query.
        """

        raise NotImplementedError