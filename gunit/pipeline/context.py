"""
Pipeline execution context.
"""

from __future__ import annotations


class PipelineContext:
    """
    Shared context.
    """

    def __init__(self) -> None:
        self.items: dict[str, object] = {}

    def set(
        self,
        key: str,
        value: object,
    ) -> None:
        self.items[key] = value

    def get(
        self,
        key: str,
        default: object | None = None,
    ) -> object | None:
        return self.items.get(key, default)