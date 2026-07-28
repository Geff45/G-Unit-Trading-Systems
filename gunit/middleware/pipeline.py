"""
G-Unit Platform

Middleware Pipeline
"""

from __future__ import annotations

from collections.abc import Callable

from .context import MiddlewareContext
from .delegate import RequestDelegate
from .middleware import Middleware


class MiddlewarePipeline:
    """
    Executes middleware in registration order.
    """

    def __init__(self) -> None:

        self._middleware: list[Middleware] = []

    def add(
        self,
        middleware: Middleware,
    ) -> "MiddlewarePipeline":

        self._middleware.append(middleware)

        return self

    @property
    def count(self) -> int:

        return len(self._middleware)

    def execute(
        self,
        context: MiddlewareContext,
    ) -> None:

        def terminal(_: MiddlewareContext) -> None:
            return

        delegate: RequestDelegate = terminal

        #
        # Build the pipeline from the end.
        #

        for middleware in reversed(self._middleware):

            previous = delegate

            def make_delegate(
                current: Middleware,
                next_delegate: RequestDelegate,
            ) -> RequestDelegate:

                def invoke(ctx: MiddlewareContext) -> None:

                    if ctx.cancelled:
                        return

                    current.invoke(
                        ctx,
                        next_delegate,
                    )

                return invoke

            delegate = make_delegate(
                middleware,
                previous,
            )

        delegate(context)