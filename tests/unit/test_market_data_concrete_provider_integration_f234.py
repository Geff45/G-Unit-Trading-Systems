from gunit.di import ServiceCollection, ServiceLifetime
from gunit.modules import ModuleContext
from gunit.modules.in_memory_market_data_provider import (
    InMemoryMarketDataProvider,
)
from gunit.modules.market_data_module import (
    MarketDataModule,
    MarketDataService,
)
from gunit.modules.market_data_provider import MarketDataProvider


def test_market_data_module_preserves_concrete_provider_registration():
    services = ServiceCollection()
    context = ModuleContext(services)

    services.add(
        MarketDataProvider,
        lambda: InMemoryMarketDataProvider({"EURUSD": 1.1234}),
        lifetime=ServiceLifetime.SINGLETON,
    )

    module = MarketDataModule()
    module.configure(context)

    provider = services.build_provider()
    service = provider.get(MarketDataService)

    assert isinstance(service, MarketDataService)
    assert service.get_latest_price("EURUSD") == 1.1234

    provider.dispose()


def test_market_data_module_resolves_configured_in_memory_price():
    services = ServiceCollection()
    context = ModuleContext(services)

    services.add(
        MarketDataProvider,
        lambda: InMemoryMarketDataProvider({"EURUSD": 1.1234}),
        lifetime=ServiceLifetime.SINGLETON,
    )

    module = MarketDataModule()
    module.configure(context)

    provider = services.build_provider()
    service = provider.get(MarketDataService)

    assert service.get_latest_price("EURUSD") == 1.1234

    provider.dispose()
