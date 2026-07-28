"""
G-Unit Platform

Middleware Base Class
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from .context import MiddlewareContext
from .delegate import RequestDelegate


class Middleware(ABC):
    """
    Base class for all middleware.
    """

    @abstractmethod
    def invoke(
        self,
        context: MiddlewareContext,
        next_delegate: RequestDelegate,
    ) -> None:
        """
        Process the middleware request.

        Implementations should perform any required work and then
        invoke the next delegate unless processing should stop.
        """
        raise NotImplementedError