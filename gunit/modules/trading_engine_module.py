from __future__ import annotations

from .module import Module
from .module_context import ModuleContext


class TradingEngineModule(Module):
    """
    Atlas Trading Engine module foundation.

    Establishes the module identity and lifecycle boundary
    without introducing trading-engine implementation logic.
    """

    @property
    def name(self) -> str:
        return "TradingEngine"

    @property
    def version(self) -> str:
        return "1.0.0"

    def configure(self, context: ModuleContext) -> None:
        """
        Configure the trading engine module.

        Service registrations will be introduced by later
        trading-engine milestones.
        """
        return None

    def start(self, context: ModuleContext) -> None:
        """
        Start the trading engine module.
        """
        return None

    def stop(self, context: ModuleContext) -> None:
        """
        Stop the trading engine module.
        """
        return None
