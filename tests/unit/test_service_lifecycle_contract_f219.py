import pytest

from gunit.di import ServiceCollection, ServiceLifetime
from gunit.core.di.exceptions import ServiceResolutionError


class CloseableService:
    def __init__(self):
        self.closed = False

    def close(self):
        self.closed = True


class DisposableService:
    def __init__(self):
        self.disposed = False

    def dispose(self):
        self.disposed = True


class ContextManagedService:
    def __init__(self):
        self.exited = False

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.exited = True


class PlainService:
    pass


def build_provider(service_type, implementation_type):
    services = ServiceCollection()

    services.add(
        service_type,
        implementation_type,
        ServiceLifetime.SCOPED,
    )

    return services.build_provider()


def test_scope_dispose_closes_closeable_service():
    provider = build_provider(
        CloseableService,
        CloseableService,
    )

    scope = provider.create_scope()
    service = scope.get(CloseableService)

    scope.dispose()

    assert service.closed is True


def test_scope_dispose_disposes_disposable_service():
    provider = build_provider(
        DisposableService,
        DisposableService,
    )

    scope = provider.create_scope()
    service = scope.get(DisposableService)

    scope.dispose()

    assert service.disposed is True


def test_scope_dispose_exits_context_managed_service():
    provider = build_provider(
        ContextManagedService,
        ContextManagedService,
    )

    scope = provider.create_scope()
    service = scope.get(ContextManagedService)

    scope.dispose()

    assert service.exited is True


def test_scope_dispose_releases_plain_services():
    provider = build_provider(
        PlainService,
        PlainService,
    )

    scope = provider.create_scope()
    service = scope.get(PlainService)

    assert service is scope.get(PlainService)

    scope.dispose()

    with pytest.raises(ServiceResolutionError):
        scope.get(PlainService)


def test_scope_dispose_is_idempotent():
    provider = build_provider(
        CloseableService,
        CloseableService,
    )

    scope = provider.create_scope()
    service = scope.get(CloseableService)

    scope.dispose()
    scope.dispose()

    assert service.closed is True


def test_disposed_scope_rejects_resolution():
    provider = build_provider(
        PlainService,
        PlainService,
    )

    scope = provider.create_scope()
    scope.dispose()

    with pytest.raises(ServiceResolutionError):
        scope.get(PlainService)


def test_singleton_is_not_disposed_with_scope():
    class SingletonService:
        def __init__(self):
            self.closed = False

        def close(self):
            self.closed = True

    services = ServiceCollection()

    services.add(
        SingletonService,
        SingletonService,
        ServiceLifetime.SINGLETON,
    )

    provider = services.build_provider()
    scope = provider.create_scope()

    service = scope.get(SingletonService)

    scope.dispose()

    assert service.closed is False


def test_transient_services_are_not_scope_owned():
    class TransientService:
        def __init__(self):
            self.closed = False

        def close(self):
            self.closed = True

    services = ServiceCollection()

    services.add(
        TransientService,
        TransientService,
        ServiceLifetime.TRANSIENT,
    )

    provider = services.build_provider()
    scope = provider.create_scope()

    service = scope.get(TransientService)

    scope.dispose()

    assert service.closed is False


def test_scope_reports_disposed_state():
    provider = build_provider(
        PlainService,
        PlainService,
    )

    scope = provider.create_scope()

    assert scope.is_disposed is False

    scope.dispose()

    assert scope.is_disposed is True
