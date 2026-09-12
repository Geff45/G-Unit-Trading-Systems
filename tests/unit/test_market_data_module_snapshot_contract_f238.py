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
from gunit.modules.market_data_snapshot import MarketDataSnapshot


def test_market_data_module_routes_snapshot_requests_to_configured_provider():
    services = ServiceCollection()
    context = ModuleContext(services)

    services.add(
        MarketDataProvider,
        lambda: InMemoryMarketDataProvider({"EURUSD": 1.2345}),
        lifetime=ServiceLifetime.SINGLETON,
    )

    module = MarketDataModule()
    module.configure(context)

    provider = services.build_provider()
    service = provider.get(MarketDataService)

    snapshot = service.get_latest_snapshot("EURUSD")

    assert isinstance(snapshot, MarketDataSnapshot)
    assert snapshot.symbol == "EURUSD"
    assert snapshot.price == 1.2345

    provider.dispose()


def test_market_data_module_preserves_snapshot_capable_provider_registration():
    services = ServiceCollection()
    context = ModuleContext(services)

    services.add(
        MarketDataProvider,
        lambda: InMemoryMarketDataProvider({"EURUSD": 1.2345}),
        lifetime=ServiceLifetime.SINGLETON,
    )

    module = MarketDataModule()
    module.configure(context)

    descriptor = services.get_descriptor(MarketDataProvider)

    assert descriptor.service_type is MarketDataProvider
    assert descriptor.lifetime is ServiceLifetime.SINGLETON

    provider = services.build_provider()
    service = provider.get(MarketDataService)

    snapshot = service.get_latest_snapshot("EURUSD")

    assert isinstance(snapshot, MarketDataSnapshot)
    assert snapshot.price == 1.2345

    provider.dispose()
