from gunit.di import ServiceLifetime
from gunit.modules import Module, ModuleContext
from gunit.modules.market_data_provider import MarketDataProvider


class UnavailableMarketDataProvider(MarketDataProvider):
    """
    Default provider until a concrete market-data source is integrated.
    """

    def get_latest_price(self, symbol: str):
        raise NotImplementedError(
            "No market data provider implementation is configured"
        )


class MarketDataService:
    """
    Market-data service boundary backed by a provider.
    """

    def __init__(self, provider: MarketDataProvider) -> None:
        self._provider = provider

    @property
    def name(self) -> str:
        return "MarketDataService"

    @property
    def version(self) -> str:
        return "1.0.0"

    def get_latest_price(self, symbol: str):
        if not symbol or not symbol.strip():
            raise ValueError("symbol must not be empty")

        return self._provider.get_latest_price(symbol)


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
        if not context.services.contains(MarketDataProvider):
            context.services.add(
                MarketDataProvider,
                UnavailableMarketDataProvider,
                lifetime=ServiceLifetime.SINGLETON,
            )

        context.services.add(
            MarketDataService,
            MarketDataService,
            lifetime=ServiceLifetime.SINGLETON,
        )

    def start(self, context: ModuleContext) -> None:
        return None

    def stop(self, context: ModuleContext) -> None:
        return None
