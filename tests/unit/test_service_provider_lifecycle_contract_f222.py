from gunit.di import ServiceCollection, ServiceLifetime
from gunit.core.di.exceptions import ServiceResolutionError


class CloseableSingleton:
    def __init__(self):
        self.closed = False

    def close(self):
        self.closed = True


class DisposableSingleton:
    def __init__(self):
        self.disposed = False

    def dispose(self):
        self.disposed = True


class ContextManagedSingleton:
    def __init__(self):
        self.exited = False

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.exited = True


class PlainSingleton:
    pass


def test_provider_exposes_dispose():
    provider = ServiceCollection().build_provider()

    assert hasattr(provider, "dispose")


def test_provider_reports_disposed_state():
    provider = ServiceCollection().build_provider()

    assert hasattr(provider, "is_disposed")
    assert provider.is_disposed is False

    provider.dispose()

    assert provider.is_disposed is True


def test_provider_disposes_singleton_with_close():
    services = ServiceCollection()

    services.add(
        CloseableSingleton,
        CloseableSingleton,
        ServiceLifetime.SINGLETON,
    )

    provider = services.build_provider()
    instance = provider.get(CloseableSingleton)

    provider.dispose()

    assert instance.closed is True


def test_provider_disposes_singleton_with_dispose():
    services = ServiceCollection()

    services.add(
        DisposableSingleton,
        DisposableSingleton,
        ServiceLifetime.SINGLETON,
    )

    provider = services.build_provider()
    instance = provider.get(DisposableSingleton)

    provider.dispose()

    assert instance.disposed is True


def test_provider_disposes_singleton_with_context_manager():
    services = ServiceCollection()

    services.add(
        ContextManagedSingleton,
        ContextManagedSingleton,
        ServiceLifetime.SINGLETON,
    )

    provider = services.build_provider()
    instance = provider.get(ContextManagedSingleton)

    provider.dispose()

    assert instance.exited is True


def test_provider_dispose_is_idempotent():
    services = ServiceCollection()

    services.add(
        CloseableSingleton,
        CloseableSingleton,
        ServiceLifetime.SINGLETON,
    )

    provider = services.build_provider()
    instance = provider.get(CloseableSingleton)

    provider.dispose()
    provider.dispose()

    assert instance.closed is True


def test_disposed_provider_rejects_resolution():
    services = ServiceCollection()

    services.add(
        PlainSingleton,
        PlainSingleton,
        ServiceLifetime.SINGLETON,
    )

    provider = services.build_provider()
    provider.dispose()

    try:
        provider.get(PlainSingleton)
    except ServiceResolutionError:
        return

    raise AssertionError(
        "Disposed provider must reject service resolution"
    )


def test_provider_disposal_does_not_dispose_transient_services():
    services = ServiceCollection()

    services.add(
        CloseableSingleton,
        CloseableSingleton,
        ServiceLifetime.TRANSIENT,
    )

    provider = services.build_provider()
    instance = provider.get(CloseableSingleton)

    provider.dispose()

    assert instance.closed is False
