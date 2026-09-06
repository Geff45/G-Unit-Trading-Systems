import pytest

from gunit.di import ServiceCollection, ServiceLifetime
from gunit.host import Host, HostBuilder
from gunit.host.options import HostOptions


class SingletonService:
    pass


class ScopedService:
    pass


class TransientService:
    pass


def test_host_builder_exposes_service_collection():
    builder = HostBuilder()

    assert isinstance(builder.services, ServiceCollection)


def test_host_build_creates_provider():
    builder = HostBuilder()

    host = builder.build()

    assert hasattr(host, "provider")
    assert host.provider is not None


def test_host_provider_resolves_registered_singleton():
    builder = HostBuilder()

    builder.services.add(
        SingletonService,
        SingletonService,
        ServiceLifetime.SINGLETON,
    )

    host = builder.build()

    first = host.provider.get(SingletonService)
    second = host.provider.get(SingletonService)

    assert first is second


def test_host_provider_resolves_transient_service():
    builder = HostBuilder()

    builder.services.add(
        TransientService,
        TransientService,
        ServiceLifetime.TRANSIENT,
    )

    host = builder.build()

    first = host.provider.get(TransientService)
    second = host.provider.get(TransientService)

    assert first is not second


def test_host_creates_scoped_service_scope():
    builder = HostBuilder()

    builder.services.add(
        ScopedService,
        ScopedService,
        ServiceLifetime.SCOPED,
    )

    host = builder.build()

    scope = host.create_scope()

    first = scope.get(ScopedService)
    second = scope.get(ScopedService)

    assert first is second


def test_host_scopes_are_isolated():
    builder = HostBuilder()

    builder.services.add(
        ScopedService,
        ScopedService,
        ServiceLifetime.SCOPED,
    )

    host = builder.build()

    first_scope = host.create_scope()
    second_scope = host.create_scope()

    first = first_scope.get(ScopedService)
    second = second_scope.get(ScopedService)

    assert first is not second


def test_host_preserves_options():
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


def test_host_start_and_stop_remain_functional():
    host = HostBuilder().build()

    host.start()

    assert host.running

    host.stop()

    assert not host.running


def test_host_exposes_service_collection_for_registration():
    builder = HostBuilder()

    builder.services.add(
        SingletonService,
        SingletonService,
        ServiceLifetime.SINGLETON,
    )

    host = builder.build()

    assert host.provider.get(SingletonService) is not None
