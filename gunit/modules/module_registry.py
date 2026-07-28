"""
Module registry.
"""

from __future__ import annotations

from .module import Module


class ModuleRegistry:
    """
    Stores Atlas modules.
    """

    def __init__(self) -> None:
        self._modules: list[Module] = []

    def register(self, module: Module) -> None:
        self._modules.append(module)

    @property
    def modules(self) -> list[Module]:
        return list(self._modules)