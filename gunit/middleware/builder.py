"""
G-Unit Platform

Middleware Pipeline Builder
"""

from __future__ import annotations

from .middleware import Middleware
from .pipeline import MiddlewarePipeline


class MiddlewareBuilder:
    """
    Fluent middleware builder.
    """

    def __init__(self) -> None:

        self._pipeline = MiddlewarePipeline()

    def use(
        self,
        middleware: Middleware,
    ) -> "MiddlewareBuilder":

        self._pipeline.add(middleware)

        return self

    def build(self) -> MiddlewarePipeline:

        return self._pipeline