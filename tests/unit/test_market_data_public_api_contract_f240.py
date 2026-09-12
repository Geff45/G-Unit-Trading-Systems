def test_market_data_module_is_publicly_exported():
    from gunit.modules import MarketDataModule

    assert MarketDataModule is not None


def test_market_data_service_is_publicly_exported():
    from gunit.modules import MarketDataService

    assert MarketDataService is not None


def test_market_data_provider_is_publicly_exported():
    from gunit.modules import MarketDataProvider

    assert MarketDataProvider is not None


def test_market_data_snapshot_is_publicly_exported():
    from gunit.modules import MarketDataSnapshot

    assert MarketDataSnapshot is not None


def test_in_memory_market_data_provider_is_publicly_exported():
    from gunit.modules import InMemoryMarketDataProvider

    assert InMemoryMarketDataProvider is not None
