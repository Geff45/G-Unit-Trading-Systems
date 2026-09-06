from gunit.di import ServiceCollection, ServiceLifetime
from gunit.modules import ModuleContext

from gunit.modules.market_data_module import (
    MarketDataModule,
    MarketDataService,
)


def test_market_data_service_is_registered_as_singleton():
    services = ServiceCollection()
    context = ModuleContext(services)

    module = MarketDataModule()
    module.configure(context)

    descriptor = services.get_descriptor(MarketDataService)

    assert descriptor.lifetime is ServiceLifetime.SINGLETON


def test_market_data_service_resolves_from_module_configured_provider():
    services = ServiceCollection()
    context = ModuleContext(services)

    module = MarketDataModule()
    module.configure(context)

    provider = services.build_provider()

    service = provider.get(MarketDataService)

    assert isinstance(service, MarketDataService)

    provider.dispose()


def test_market_data_service_singleton_resolution_returns_same_instance():
    services = ServiceCollection()
    context = ModuleContext(services)

    module = MarketDataModule()
    module.configure(context)

    provider = services.build_provider()

    first = provider.get(MarketDataService)
    second = provider.get(MarketDataService)

    assert first is second

    provider.dispose()
