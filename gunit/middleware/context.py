"""
G-Unit Platform

Middleware Context

Represents the execution context passed through
the middleware pipeline.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class MiddlewareContext:
    """
    Context shared across middleware components.
    """

    services: Any | None = None

    application: Any | None = None

    host: Any | None = None

    data: dict[str, Any] = field(default_factory=dict)

    cancelled: bool = False

    def set(
        self,
        key: str,
        value: Any,
    ) -> None:
        """
        Store a value.
        """

        self.data[key] = value

    def get(
        self,
        key: str,
        default: Any = None,
    ) -> Any:
        """
        Retrieve a value.
        """

        return self.data.get(key, default)

    def contains(
        self,
        key: str,
    ) -> bool:
        """
        Returns True if a key exists.
        """

        return key in self.data

    def remove(
        self,
        key: str,
    ) -> None:
        """
        Removes a value.
        """

        self.data.pop(key, None)

    def clear(self) -> None:
        """
        Clears all stored data.
        """

        self.data.clear()

    def cancel(self) -> None:
        """
        Stops pipeline execution.
        """

        self.cancelled = True