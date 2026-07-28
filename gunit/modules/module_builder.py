"""
Module builder.
"""

from __future__ import annotations

from .module import Module
from .module_registry import ModuleRegistry


class ModuleBuilder:
    """
    Builds the module registry.
    """

    def __init__(self) -> None:
        self._registry = ModuleRegistry()

    def add(self, module: Module) -> "ModuleBuilder":
        self._registry.register(module)
        return self

    def build(self) -> ModuleRegistry:
        return self._registry