from gunit.di import ServiceCollection
from gunit.modules import ModuleContext, ModuleManager

from gunit.modules.market_data_module import (
    MarketDataModule,
    MarketDataService,
)


def test_market_data_module_integrates_with_module_manager():
    services = ServiceCollection()
    context = ModuleContext(services)

    manager = ModuleManager()
    module = MarketDataModule()

    manager.add(module)
    manager.configure(context)

    provider = services.build_provider()

    service = provider.get(MarketDataService)

    assert isinstance(service, MarketDataService)

    provider.dispose()


def test_market_data_module_remains_resolvable_through_full_manager_lifecycle():
    services = ServiceCollection()
    context = ModuleContext(services)

    manager = ModuleManager()
    manager.add(MarketDataModule())

    manager.configure(context)
    manager.start(context)

    provider = services.build_provider()

    service = provider.get(MarketDataService)

    assert isinstance(service, MarketDataService)

    manager.stop(context)
    provider.dispose()
