from gunit.configuration import ConfigurationProvider


def test_configuration_provider():
    provider = ConfigurationProvider()

    assert provider.load() == {}
