from gunit.configuration import EnvironmentProvider


def test_environment_provider():
    provider = EnvironmentProvider()

    assert isinstance(provider.load(), dict)
