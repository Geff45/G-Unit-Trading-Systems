"""
Atlas Forge Dependency Container

Version: 1.0.0
"""

from __future__ import annotations

from typing import Any


class DependencyContainer:
    """
    Stores and resolves application dependencies.
    """

    def __init__(self) -> None:
        self._services: dict[str, Any] = {}

    def register(self, name: str, instance: Any) -> None:
        if name in self._services:
            raise ValueError(
                f"Dependency '{name}' already registered."
            )

        self._services[name] = instance

    def resolve(self, name: str) -> Any:
        try:
            return self._services[name]
        except KeyError as exc:
            raise KeyError(
                f"Dependency '{name}' not found."
            ) from exc

    def unregister(self, name: str) -> None:
        self._services.pop(name, None)

    def exists(self, name: str) -> bool:
        return name in self._services

    def count(self) -> int:
        return len(self._services)

    def clear(self) -> None:
        self._services.clear()

    def list_dependencies(self) -> list[str]:
        return sorted(self._services.keys())