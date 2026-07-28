from __future__ import annotations

from typing import Dict, Iterable, Optional

from .plugin import Plugin


class PluginRegistry:
    """
    Stores all loaded plugin instances.

    Responsible only for registration and lookup.
    Lifecycle management remains the responsibility
    of PluginManager.
    """

    def __init__(self) -> None:
        self._plugins: Dict[str, Plugin] = {}

    def register(self, plugin: Plugin) -> None:
        name = plugin.descriptor.name

        if name in self._plugins:
            raise ValueError(f"Plugin '{name}' already registered.")

        self._plugins[name] = plugin

    def unregister(self, name: str) -> None:
        self._plugins.pop(name, None)

    def get(self, name: str) -> Optional[Plugin]:
        return self._plugins.get(name)

    def contains(self, name: str) -> bool:
        return name in self._plugins

    def clear(self) -> None:
        self._plugins.clear()

    def all(self) -> Iterable[Plugin]:
        return self._plugins.values()

    def names(self) -> list[str]:
        return list(self._plugins.keys())

    def count(self) -> int:
        return len(self._plugins)