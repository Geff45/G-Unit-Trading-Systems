from gunit.di import (
    ServiceCollection,
    ServiceDescriptor,
    ServiceLifetime,
    ServiceProvider,
)


class DemoService:
    pass


def test_service_lifetime_values():
    assert ServiceLifetime.TRANSIENT.value == "transient"
    assert ServiceLifetime.SINGLETON.value == "singleton"
    assert ServiceLifetime.SCOPED.value == "scoped"


def test_service_descriptor_can_describe_service():
    descriptor = ServiceDescriptor(
        service_type=DemoService,
        implementation_type=DemoService,
        lifetime=ServiceLifetime.TRANSIENT,
    )

    assert descriptor.service_type is DemoService
    assert descriptor.implementation_type is DemoService
    assert descriptor.lifetime is ServiceLifetime.TRANSIENT


def test_service_collection_can_register_service():
    services = ServiceCollection()

    services.add(
        DemoService,
        DemoService,
        ServiceLifetime.TRANSIENT,
    )

    assert services.contains(DemoService)


def test_service_collection_can_build_provider():
    services = ServiceCollection()

    services.add(
        DemoService,
        DemoService,
        ServiceLifetime.TRANSIENT,
    )

    provider = services.build_provider()

    assert isinstance(provider, ServiceProvider)


def test_transient_resolution_creates_new_instance():
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


def test_singleton_resolution_reuses_instance():
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


def test_unregistered_service_raises_resolution_error():
    services = ServiceCollection()
    provider = services.build_provider()

    try:
        provider.get(DemoService)
    except Exception as exc:
        assert exc.__class__.__name__ == "ServiceResolutionError"
    else:
        raise AssertionError(
            "Expected ServiceResolutionError"
        )


def test_gunit_di_exports_are_available():
    from gunit import di

    assert di.ServiceCollection is ServiceCollection
    assert di.ServiceProvider is ServiceProvider
    assert di.ServiceDescriptor is ServiceDescriptor
    assert di.ServiceLifetime is ServiceLifetime
