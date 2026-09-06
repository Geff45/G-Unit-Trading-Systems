import pytest

from gunit.core.di.exceptions import ServiceResolutionError
from gunit.di import ServiceCollection, ServiceLifetime
from gunit.modules import ModuleContext

from gunit.modules.market_data_module import (
    MarketDataModule,
    MarketDataService,
)


def _build_market_data_provider():
    services = ServiceCollection()
    context = ModuleContext(services)

    module = MarketDataModule()
    module.configure(context)

    return services, services.build_provider()


def test_market_data_service_registration_is_owned_by_market_data_module():
    services, provider = _build_market_data_provider()

    assert services.contains(MarketDataService)

    descriptor = services.get_descriptor(MarketDataService)

    assert descriptor.service_type is MarketDataService
    assert descriptor.implementation_type is MarketDataService
    assert descriptor.lifetime is ServiceLifetime.SINGLETON

    provider.dispose()


def test_market_data_service_resolves_from_module_configured_provider():
    _, provider = _build_market_data_provider()

    service = provider.get(MarketDataService)

    assert isinstance(service, MarketDataService)

    provider.dispose()


def test_disposed_market_data_provider_rejects_market_data_resolution():
    _, provider = _build_market_data_provider()

    provider.dispose()

    with pytest.raises(ServiceResolutionError):
        provider.get(MarketDataService)
