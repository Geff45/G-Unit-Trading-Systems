import pytest

from gunit.di import (
    ServiceCollection,
    ServiceLifetime,
)
from gunit.core.di.exceptions import ServiceResolutionError


class SingletonService:
    pass


class ScopedService:
    pass


class TransientService:
    pass


def build_provider():
    services = ServiceCollection()

    services.add(
        SingletonService,
        SingletonService,
        ServiceLifetime.SINGLETON,
    )

    services.add(
        ScopedService,
        ScopedService,
        ServiceLifetime.SCOPED,
    )

    services.add(
        TransientService,
        TransientService,
        ServiceLifetime.TRANSIENT,
    )

    return services.build_provider()


def test_provider_exposes_scope_creation():
    provider = build_provider()

    assert hasattr(provider, "create_scope")


def test_scope_can_resolve_registered_service():
    provider = build_provider()

    scope = provider.create_scope()

    service = scope.get(ScopedService)

    assert isinstance(service, ScopedService)


def test_scoped_service_is_shared_within_same_scope():
    provider = build_provider()

    scope = provider.create_scope()

    first = scope.get(ScopedService)
    second = scope.get(ScopedService)

    assert first is second


def test_scoped_service_is_isolated_between_scopes():
    provider = build_provider()

    first_scope = provider.create_scope()
    second_scope = provider.create_scope()

    first = first_scope.get(ScopedService)
    second = second_scope.get(ScopedService)

    assert first is not second


def test_singleton_is_shared_across_scopes():
    provider = build_provider()

    first_scope = provider.create_scope()
    second_scope = provider.create_scope()

    first = first_scope.get(SingletonService)
    second = second_scope.get(SingletonService)

    assert first is second


def test_transient_is_new_within_same_scope():
    provider = build_provider()

    scope = provider.create_scope()

    first = scope.get(TransientService)
    second = scope.get(TransientService)

    assert first is not second


def test_transient_is_new_across_scopes():
    provider = build_provider()

    first_scope = provider.create_scope()
    second_scope = provider.create_scope()

    first = first_scope.get(TransientService)
    second = second_scope.get(TransientService)

    assert first is not second


def test_root_provider_can_still_resolve_singleton():
    provider = build_provider()

    first = provider.get(SingletonService)
    second = provider.get(SingletonService)

    assert first is second


def test_missing_service_from_scope_raises_resolution_error():
    provider = build_provider()

    scope = provider.create_scope()

    class UnknownService:
        pass

    with pytest.raises(ServiceResolutionError):
        scope.get(UnknownService)
