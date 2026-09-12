import pytest

from gunit.di import ServiceCollection, ServiceLifetime
from gunit.modules import ModuleContext

from gunit.modules.market_data_module import (
    MarketDataModule,
    MarketDataService,
)
from gunit.modules.market_data_provider import MarketDataProvider


class TestMarketDataProvider(MarketDataProvider):

    def get_latest_price(self, symbol: str):
        return 123.45


def test_market_data_provider_is_registered_by_market_data_module():
    services = ServiceCollection()
    context = ModuleContext(services)

    module = MarketDataModule()
    module.configure(context)

    assert services.contains(MarketDataProvider)

    descriptor = services.get_descriptor(MarketDataProvider)

    assert descriptor.service_type is MarketDataProvider
    assert descriptor.lifetime is ServiceLifetime.SINGLETON


def test_market_data_service_resolves_with_registered_market_data_provider():
    services = ServiceCollection()
    context = ModuleContext(services)

    services.add(
        MarketDataProvider,
        TestMarketDataProvider,
        lifetime=ServiceLifetime.SINGLETON,
    )

    module = MarketDataModule()
    module.configure(context)

    provider = services.build_provider()
    service = provider.get(MarketDataService)

    assert isinstance(service, MarketDataService)
    assert service.get_latest_price("EURUSD") == 123.45

    provider.dispose()


def test_market_data_service_rejects_blank_symbol_before_provider_call():
    services = ServiceCollection()
    context = ModuleContext(services)

    services.add(
        MarketDataProvider,
        TestMarketDataProvider,
        lifetime=ServiceLifetime.SINGLETON,
    )

    module = MarketDataModule()
    module.configure(context)

    provider = services.build_provider()
    service = provider.get(MarketDataService)

    with pytest.raises(ValueError):
        service.get_latest_price("   ")

    provider.dispose()
