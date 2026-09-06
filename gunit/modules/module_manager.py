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

    def configure(self, context: ModuleContext) -> None:
        """
        Configure all registered modules using the shared context.

        Modules are configured in registration order.
        """
        for module in self._modules:
            module.configure(context)

    def start(self, context: ModuleContext) -> None:
        for module in self._modules:
            module.start(context)

    def stop(self, context: ModuleContext) -> None:
        for module in reversed(self._modules):
            module.stop(context)