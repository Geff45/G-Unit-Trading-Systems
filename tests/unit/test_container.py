from gunit.core.container import (
    ServiceContainer,
    ServiceLifetime,
)


class TestService:
    pass


def test_transient_service_creation():

    container = ServiceContainer()

    container.register(
        TestService,
        TestService,
        ServiceLifetime.TRANSIENT,
    )

    first = container.resolve(TestService)
    second = container.resolve(TestService)

    assert first is not second


def test_singleton_service_creation():

    container = ServiceContainer()

    container.register(
        TestService,
        TestService,
        ServiceLifetime.SINGLETON,
    )

    first = container.resolve(TestService)
    second = container.resolve(TestService)

    assert first is second