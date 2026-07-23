"""
Capability Registry
"""

from __future__ import annotations


class CapabilityRegistry:
    """
    Stores capabilities provided by services.
    """

    def __init__(self) -> None:
        self._capabilities: dict[str, list[str]] = {}

    def register(
        self,
        name: str,
        services: list[str] | None = None,
    ) -> None:
        self._capabilities[name] = services or []

    def unregister(self, name: str) -> None:
        self._capabilities.pop(name, None)

    def exists(self, name: str) -> bool:
        return name in self._capabilities

    def get(self, name: str) -> list[str]:
        return self._capabilities.get(name, [])

    def names(self) -> list[str]:
        return sorted(self._capabilities.keys())

    def clear(self) -> None:
        self._capabilities.clear()

    def __contains__(self, item: str) -> bool:
        return self.exists(item)

    def __len__(self) -> int:
        return len(self._capabilities)