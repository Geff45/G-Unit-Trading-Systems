"""
Atlas runtime service.
"""

from __future__ import annotations

from gunit.core.runtime.runtime import Runtime


class RuntimeService:
    """
    Atlas wrapper around Runtime.
    """

    def __init__(self) -> None:
        self._runtime = Runtime()

    @property
    def runtime(self) -> Runtime:
        return self._runtime