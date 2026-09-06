import pytest

from gunit.di import (
    ServiceCollection,
    ServiceLifetime,
)
from gunit.core.di.exceptions import ServiceResolutionError


class Database:
    pass


class Repository:
    def __init__(self, database: Database):
        self.database = database


class Service:
    def __init__(self, repository: Repository):
        self.repository = repository


class SingletonDependency:
    pass


class SingletonConsumer:
    def __init__(self, dependency: SingletonDependency):
        self.dependency = dependency


class TransientDependency:
    pass


class TransientConsumer:
    def __init__(self, dependency: TransientDependency):
        self.dependency = dependency


class MissingDependency:
    pass


class MissingConsumer:
    def __init__(self, dependency: MissingDependency):
        self.dependency = dependency


class CircularA:
    def __init__(self, dependency: "CircularB"):
        self.dependency = dependency


class CircularB:
    def __init__(self, dependency: CircularA):
        self.dependency = dependency


def test_provider_resolves_service_without_dependencies():
    services = ServiceCollection()

    services.add(
        Database,
        Database,
        ServiceLifetime.TRANSIENT,
    )

    provider = services.build_provider()

    assert isinstance(provider.get(Database), Database)


def test_provider_resolves_constructor_dependency():
    services = ServiceCollection()

    services.add(
        Database,
        Database,
        ServiceLifetime.SINGLETON,
    )

    services.add(
        Repository,
        Repository,
        ServiceLifetime.TRANSIENT,
    )

    provider = services.build_provider()

    repository = provider.get(Repository)

    assert isinstance(repository, Repository)
    assert isinstance(repository.database, Database)


def test_provider_resolves_dependency_chain():
    services = ServiceCollection()

    services.add(
        Database,
        Database,
        ServiceLifetime.SINGLETON,
    )

    services.add(
        Repository,
        Repository,
        ServiceLifetime.TRANSIENT,
    )

    services.add(
        Service,
        Service,
        ServiceLifetime.TRANSIENT,
    )

    provider = services.build_provider()

    service = provider.get(Service)

    assert isinstance(service, Service)
    assert isinstance(service.repository, Repository)
    assert isinstance(service.repository.database, Database)


def test_singleton_dependency_is_shared_when_injected():
    services = ServiceCollection()

    services.add(
        SingletonDependency,
        SingletonDependency,
        ServiceLifetime.SINGLETON,
    )

    services.add(
        SingletonConsumer,
        SingletonConsumer,
        ServiceLifetime.TRANSIENT,
    )

    provider = services.build_provider()

    first = provider.get(SingletonConsumer)
    second = provider.get(SingletonConsumer)

    assert first.dependency is second.dependency


def test_transient_dependency_is_new_when_resolved():
    services = ServiceCollection()

    services.add(
        TransientDependency,
        TransientDependency,
        ServiceLifetime.TRANSIENT,
    )

    services.add(
        TransientConsumer,
        TransientConsumer,
        ServiceLifetime.TRANSIENT,
    )

    provider = services.build_provider()

    first = provider.get(TransientConsumer)
    second = provider.get(TransientConsumer)

    assert first.dependency is not second.dependency


def test_missing_dependency_raises_service_resolution_error():
    services = ServiceCollection()

    services.add(
        MissingConsumer,
        MissingConsumer,
        ServiceLifetime.TRANSIENT,
    )

    provider = services.build_provider()

    with pytest.raises(ServiceResolutionError):
        provider.get(MissingConsumer)


def test_circular_dependency_raises_service_resolution_error():
    services = ServiceCollection()

    services.add(
        CircularA,
        CircularA,
        ServiceLifetime.TRANSIENT,
    )

    services.add(
        CircularB,
        CircularB,
        ServiceLifetime.TRANSIENT,
    )

    provider = services.build_provider()

    with pytest.raises(ServiceResolutionError):
        provider.get(CircularA)


def test_existing_f213_resolution_contract_remains_intact():
    services = ServiceCollection()

    services.add(
        Database,
        Database,
        ServiceLifetime.TRANSIENT,
    )

    provider = services.build_provider()

    first = provider.get(Database)
    second = provider.get(Database)

    assert first is not second
