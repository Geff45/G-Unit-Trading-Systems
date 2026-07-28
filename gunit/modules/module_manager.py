"""
Module manager.
"""

from __future__ import annotations

from .module import Module
from .module_context import ModuleContext


class ModuleManager:
    """
    Starts and stops Atlas modules.
    """

    def __init__(self) -> None:
        self._modules: list[Module] = []

    def add(self, module: Module) -> None:
        self._modules.append(module)

    def start(self, context: ModuleContext) -> None:
        for module in self._modules:
            module.start(context)

    def stop(self, context: ModuleContext) -> None:
        for module in reversed(self._modules):
            module.stop(context)