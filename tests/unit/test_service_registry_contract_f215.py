from gunit.di import (
    ServiceCollection,
    ServiceLifetime,
)


class DemoService:
    pass


class AnotherService:
    pass


def test_di_registration_produces_descriptor():
    services = ServiceCollection()

    services.add(
        DemoService,
        DemoService,
        ServiceLifetime.TRANSIENT,
    )

    assert services.contains(DemoService)

    descriptor = services.get_descriptor(DemoService)

    assert descriptor.service_type is DemoService
    assert descriptor.implementation_type is DemoService
    assert descriptor.lifetime is ServiceLifetime.TRANSIENT


def test_di_registration_is_type_based():
    services = ServiceCollection()

    services.add(
        DemoService,
        DemoService,
        ServiceLifetime.TRANSIENT,
    )

    assert services.contains(DemoService)
    assert not services.contains(AnotherService)


def test_provider_is_built_from_registration_layer():
    services = ServiceCollection()

    services.add(
        DemoService,
        DemoService,
        ServiceLifetime.TRANSIENT,
    )

    provider = services.build_provider()

    assert provider.get(DemoService) is not None


def test_registration_does_not_require_legacy_registry():
    services = ServiceCollection()

    services.add(
        DemoService,
        DemoService,
        ServiceLifetime.TRANSIENT,
    )

    provider = services.build_provider()

    assert provider.get(DemoService).__class__ is DemoService


def test_registration_preserves_lifetime():
    services = ServiceCollection()

    services.add(
        DemoService,
        DemoService,
        ServiceLifetime.SINGLETON,
    )

    provider = services.build_provider()

    first = provider.get(DemoService)
    second = provider.get(DemoService)

    assert first is second


def test_transient_registration_creates_new_instances():
    services = ServiceCollection()

    services.add(
        DemoService,
        DemoService,
        ServiceLifetime.TRANSIENT,
    )

    provider = services.build_provider()

    first = provider.get(DemoService)
    second = provider.get(DemoService)

    assert first is not second


def test_multiple_services_have_independent_registrations():
    services = ServiceCollection()

    services.add(
        DemoService,
        DemoService,
        ServiceLifetime.SINGLETON,
    )

    services.add(
        AnotherService,
        AnotherService,
        ServiceLifetime.TRANSIENT,
    )

    provider = services.build_provider()

    assert provider.get(DemoService).__class__ is DemoService
    assert provider.get(AnotherService).__class__ is AnotherService


def test_service_collection_returns_itself_for_chaining():
    services = ServiceCollection()

    result = services.add(
        DemoService,
        DemoService,
        ServiceLifetime.TRANSIENT,
    )

    assert result is services
