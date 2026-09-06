import pytest

from gunit.di import (
    ServiceCollection,
    ServiceLifetime,
)
from gunit.core.di.exceptions import ServiceResolutionError


class Database:
    def __init__(self):
        self.value = "database"


class Repository:
    def __init__(self, database: Database):
        self.database = database


class FactoryProduct:
    def __init__(self, value):
        self.value = value


def database_factory():
    return Database()


def repository_factory():
    return Repository(Database())


def test_factory_registration_is_available():
    services = ServiceCollection()

    services.add_factory(
        Database,
        database_factory,
        ServiceLifetime.TRANSIENT,
    )

    assert services.contains(Database)


def test_factory_resolution_returns_created_instance():
    services = ServiceCollection()

    services.add_factory(
        Database,
        database_factory,
        ServiceLifetime.TRANSIENT,
    )

    provider = services.build_provider()

    database = provider.get(Database)

    assert isinstance(database, Database)
    assert database.value == "database"


def test_transient_factory_creates_new_instance():
    services = ServiceCollection()

    services.add_factory(
        Database,
        database_factory,
        ServiceLifetime.TRANSIENT,
    )

    provider = services.build_provider()

    first = provider.get(Database)
    second = provider.get(Database)

    assert first is not second


def test_singleton_factory_reuses_instance():
    services = ServiceCollection()

    services.add_factory(
        Database,
        database_factory,
        ServiceLifetime.SINGLETON,
    )

    provider = services.build_provider()

    first = provider.get(Database)
    second = provider.get(Database)

    assert first is second


def test_factory_can_create_dependency_graph():
    services = ServiceCollection()

    services.add_factory(
        Repository,
        repository_factory,
        ServiceLifetime.TRANSIENT,
    )

    provider = services.build_provider()

    repository = provider.get(Repository)

    assert isinstance(repository, Repository)
    assert isinstance(repository.database, Database)


def test_factory_exception_becomes_service_resolution_error():
    def failing_factory():
        raise RuntimeError("factory failed")

    services = ServiceCollection()

    services.add_factory(
        Database,
        failing_factory,
        ServiceLifetime.TRANSIENT,
    )

    provider = services.build_provider()

    with pytest.raises(ServiceResolutionError):
        provider.get(Database)


def test_existing_type_registration_remains_intact():
    services = ServiceCollection()

    services.add(
        Database,
        Database,
        ServiceLifetime.TRANSIENT,
    )

    provider = services.build_provider()

    first = provider.get(Database)
    second = provider.get(Database)

    assert isinstance(first, Database)
    assert first is not second
