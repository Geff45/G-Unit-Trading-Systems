from gunit.di import ServiceLifetime
from gunit.modules import Module, ModuleContext


class MarketDataService:
    """
    Minimal market-data service boundary.

    Implementation will be introduced by later milestones.
    """


class MarketDataModule(Module):
    """
    Atlas market-data module foundation.
    """

    @property
    def name(self) -> str:
        return "MarketDataModule"

    @property
    def version(self) -> str:
        return "1.0.0"

    def configure(self, context: ModuleContext) -> None:
        context.services.add(
            MarketDataService,
            MarketDataService,
            lifetime=ServiceLifetime.SINGLETON,
        )

    def start(self, context: ModuleContext) -> None:
        return None

    def stop(self, context: ModuleContext) -> None:
        return None
