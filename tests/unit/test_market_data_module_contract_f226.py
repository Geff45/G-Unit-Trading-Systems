from gunit.di import ServiceCollection, ServiceLifetime
from gunit.modules import ModuleContext

from gunit.modules.market_data_module import (
    MarketDataModule,
    MarketDataService,
)


def test_market_data_module_registers_service_with_shared_di_context():
    services = ServiceCollection()
    context = ModuleContext(services)
    module = MarketDataModule()

    module.configure(context)

    assert services.contains(MarketDataService)

    descriptor = services.get_descriptor(MarketDataService)

    assert descriptor.service_type is MarketDataService
    assert descriptor.implementation_type is MarketDataService
    assert descriptor.lifetime is ServiceLifetime.SINGLETON


def test_market_data_module_registered_service_is_resolvable():
    services = ServiceCollection()
    context = ModuleContext(services)
    module = MarketDataModule()

    module.configure(context)

    provider = services.build_provider()

    service = provider.get(MarketDataService)

    assert isinstance(service, MarketDataService)

    provider.dispose()
