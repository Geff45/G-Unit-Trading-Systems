"""
Application environment.
"""

from __future__ import annotations


class ApplicationEnvironment:
    """
    Represents the current application environment.
    """

    def __init__(self, name: str = "Development") -> None:
        self._name = name

    @property
    def name(self) -> str:
        return self._name

    @property
    def is_development(self) -> bool:
        return self._name.lower() == "development"

    @property
    def is_testing(self) -> bool:
        return self._name.lower() == "testing"

    @property
    def is_production(self) -> bool:
        return self._name.lower() == "production"

    def __str__(self) -> str:
        return self._name