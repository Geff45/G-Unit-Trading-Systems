import pytest

from gunit.di import ServiceCollection, ServiceLifetime
from gunit.host import Host, HostBuilder
from gunit.host.hosted_service import HostedService
from gunit.host.options import HostOptions


class Dependency:
    pass


class DIHostedService(HostedService):
    def __init__(self, dependency: Dependency):
        self.dependency = dependency
        self.started = False
        self.stopped = False

    def start(self) -> None:
        self.started = True

    def stop(self) -> None:
        self.stopped = True


class SecondHostedService(HostedService):
    def __init__(self):
        self.started = False
        self.stopped = False

    def start(self) -> None:
        self.started = True

    def stop(self) -> None:
        self.stopped = True


def test_host_builder_can_register_hosted_service_through_di():
    builder = HostBuilder()

    builder.services.add(
        Dependency,
        Dependency,
        ServiceLifetime.SINGLETON,
    )
    builder.services.add(
        DIHostedService,
        DIHostedService,
        ServiceLifetime.SINGLETON,
    )

    host = builder.build()

    service = host.provider.get(DIHostedService)

    assert isinstance(service, DIHostedService)
    assert isinstance(service.dependency, Dependency)


def test_host_resolves_constructor_dependency_for_hosted_service():
    builder = HostBuilder()

    builder.services.add(
        Dependency,
        Dependency,
        ServiceLifetime.SINGLETON,
    )
    builder.services.add(
        DIHostedService,
        DIHostedService,
        ServiceLifetime.SINGLETON,
    )

    host = builder.build()

    service = host.provider.get(DIHostedService)

    assert service.dependency is host.provider.get(Dependency)


def test_host_registers_resolved_hosted_service():
    builder = HostBuilder()

    builder.services.add(
        Dependency,
        Dependency,
        ServiceLifetime.SINGLETON,
    )
    builder.services.add(
        DIHostedService,
        DIHostedService,
        ServiceLifetime.SINGLETON,
    )

    host = builder.build()

    service = host.provider.get(DIHostedService)

    host.add_hosted_service(service)

    assert service in host.hosted_services.services


def test_host_starts_di_resolved_hosted_service():
    builder = HostBuilder()

    builder.services.add(
        Dependency,
        Dependency,
        ServiceLifetime.SINGLETON,
    )
    builder.services.add(
        DIHostedService,
        DIHostedService,
        ServiceLifetime.SINGLETON,
    )

    host = builder.build()
    service = host.provider.get(DIHostedService)

    host.add_hosted_service(service)
    host.start()

    assert service.started


def test_host_stops_di_resolved_hosted_service():
    builder = HostBuilder()

    builder.services.add(
        Dependency,
        Dependency,
        ServiceLifetime.SINGLETON,
    )
    builder.services.add(
        DIHostedService,
        DIHostedService,
        ServiceLifetime.SINGLETON,
    )

    host = builder.build()
    service = host.provider.get(DIHostedService)

    host.add_hosted_service(service)
    host.start()
    host.stop()

    assert service.stopped


def test_host_supports_multiple_di_hosted_services():
    builder = HostBuilder()

    builder.services.add(
        Dependency,
        Dependency,
        ServiceLifetime.SINGLETON,
    )
    builder.services.add(
        DIHostedService,
        DIHostedService,
        ServiceLifetime.SINGLETON,
    )
    builder.services.add(
        SecondHostedService,
        SecondHostedService,
        ServiceLifetime.SINGLETON,
    )

    host = builder.build()

    first = host.provider.get(DIHostedService)
    second = host.provider.get(SecondHostedService)

    host.add_hosted_service(first)
    host.add_hosted_service(second)

    host.start()

    assert first.started
    assert second.started


def test_host_preserves_existing_manual_hosted_service_registration():
    builder = HostBuilder()
    host = builder.build()

    service = SecondHostedService()

    host.add_service(service)
    host.start()

    assert service.started

    host.stop()

    assert service.stopped


def test_hosted_service_is_singleton_when_registered_as_singleton():
    builder = HostBuilder()

    builder.services.add(
        Dependency,
        Dependency,
        ServiceLifetime.SINGLETON,
    )
    builder.services.add(
        DIHostedService,
        DIHostedService,
        ServiceLifetime.SINGLETON,
    )

    host = builder.build()

    first = host.provider.get(DIHostedService)
    second = host.provider.get(DIHostedService)

    assert first is second
