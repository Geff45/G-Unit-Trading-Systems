from gunit.di import ServiceCollection, ServiceLifetime
from gunit.modules import (
    Module,
    ModuleBuilder,
    ModuleContext,
    ModuleManager,
)


class RecordingService:
    pass


class SecondService:
    pass


class ConfigurableModule(Module):
    def __init__(self, module_name: str = "TestModule"):
        self._name = module_name
        self.configured = False
        self.started = False
        self.stopped = False

    @property
    def name(self) -> str:
        return self._name

    def configure(self, context: ModuleContext) -> None:
        self.configured = True

        context.services.add(
            RecordingService,
            RecordingService,
            lifetime=ServiceLifetime.SINGLETON,
        )

    def start(self, context: ModuleContext) -> None:
        self.started = True

    def stop(self, context: ModuleContext) -> None:
        self.stopped = True


def test_module_context_exposes_service_collection():
    services = ServiceCollection()

    context = ModuleContext(services)

    assert context.services is services


def test_module_can_register_services_during_configuration():
    services = ServiceCollection()
    context = ModuleContext(services)
    module = ConfigurableModule()

    module.configure(context)

    provider = services.build_provider()

    resolved = provider.get(RecordingService)

    assert isinstance(resolved, RecordingService)


def test_module_registered_service_preserves_declared_lifetime():
    services = ServiceCollection()
    context = ModuleContext(services)
    module = ConfigurableModule()

    module.configure(context)

    provider = services.build_provider()

    first = provider.get(RecordingService)
    second = provider.get(RecordingService)

    assert first is second


def test_multiple_modules_can_contribute_services():
    class SecondModule(Module):
        @property
        def name(self) -> str:
            return "SecondModule"

        def configure(self, context: ModuleContext) -> None:
            context.services.add(
                SecondService,
                SecondService,
                lifetime=ServiceLifetime.TRANSIENT,
            )

    services = ServiceCollection()
    context = ModuleContext(services)

    first = ConfigurableModule("FirstModule")
    second = SecondModule()

    first.configure(context)
    second.configure(context)

    provider = services.build_provider()

    assert isinstance(
        provider.get(RecordingService),
        RecordingService,
    )
    assert isinstance(
        provider.get(SecondService),
        SecondService,
    )


def test_builder_configuration_uses_shared_service_collection():
    module = ConfigurableModule()

    builder = ModuleBuilder()
    builder.add(module)

    registry = builder.build()

    services = ServiceCollection()
    context = ModuleContext(services)

    for registered_module in registry.modules:
        registered_module.configure(context)

    provider = services.build_provider()

    assert isinstance(
        provider.get(RecordingService),
        RecordingService,
    )


def test_module_lifecycle_receives_same_context():
    services = ServiceCollection()
    context = ModuleContext(services)
    module = ConfigurableModule()

    module.configure(context)
    module.start(context)
    module.stop(context)

    assert module.configured is True
    assert module.started is True
    assert module.stopped is True


def test_manager_configures_all_modules_with_shared_context():
    services = ServiceCollection()
    context = ModuleContext(services)

    first = ConfigurableModule("FirstModule")
    second = ConfigurableModule("SecondModule")

    manager = ModuleManager()

    manager.add(first)
    manager.add(second)

    manager.configure(context)

    provider = services.build_provider()

    assert isinstance(
        provider.get(RecordingService),
        RecordingService,
    )

    assert first.configured is True
    assert second.configured is True