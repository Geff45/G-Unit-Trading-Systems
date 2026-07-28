from gunit.host.builder import HostBuilder
from gunit.host.host import Host
from gunit.host.options import HostOptions


def test_builder_creates_host():

    builder = HostBuilder()

    host = builder.build()

    assert isinstance(host, Host)


def test_builder_returns_self():

    builder = HostBuilder()

    assert builder.use_defaults() is builder


def test_builder_custom_options():

    builder = HostBuilder()

    builder.use_options(
        HostOptions(
            application_name="Atlas",
            environment="Testing",
        )
    )

    host = builder.build()

    assert host.options.application_name == "Atlas"

    assert host.options.environment == "Testing"