from gunit.di.service_collection import ServiceCollection
from gunit.modules import (
    Module,
    ModuleBuilder,
    ModuleContext,
    ModuleDescriptor,
    ModuleLoader,
    ModuleManager,
    ModuleRegistry,
    ModuleState,
)


class RecordingModule(Module):
    def __init__(self, module_name: str = "TestModule"):
        self._name = module_name
        self.events = []

    @property
    def name(self) -> str:
        return self._name

    def configure(self, context: ModuleContext) -> None:
        self.events.append("configure")

    def start(self, context: ModuleContext) -> None:
        self.events.append("start")

    def stop(self, context: ModuleContext) -> None:
        self.events.append("stop")


def test_module_contract_exposes_identity_and_lifecycle():
    module = RecordingModule()

    assert module.name == "TestModule"
    assert module.version == "1.0.0"

    context = ModuleContext(ServiceCollection())

    module.configure(context)
    module.start(context)
    module.stop(context)

    assert module.events == [
        "configure",
        "start",
        "stop",
    ]


def test_module_descriptor_represents_module_identity():
    descriptor = ModuleDescriptor(
        name="Trading",
        version="2.0.0",
    )

    assert descriptor.name == "Trading"
    assert descriptor.version == "2.0.0"


def test_module_states_are_canonical():
    assert ModuleState.CREATED.value == "created"
    assert ModuleState.LOADED.value == "loaded"
    assert ModuleState.STARTED.value == "started"
    assert ModuleState.STOPPED.value == "stopped"


def test_module_context_exposes_service_collection():
    services = ServiceCollection()
    context = ModuleContext(services)

    assert context.services is services


def test_registry_registers_and_returns_modules():
    registry = ModuleRegistry()
    module = RecordingModule()

    registry.register(module)

    assert registry.modules == [module]


def test_registry_returns_snapshot_not_internal_collection():
    registry = ModuleRegistry()
    module = RecordingModule()

    registry.register(module)

    modules = registry.modules
    modules.clear()

    assert registry.modules == [module]


def test_registry_rejects_duplicate_module_names():
    registry = ModuleRegistry()

    first = RecordingModule("Trading")
    second = RecordingModule("Trading")

    registry.register(first)

    try:
        registry.register(second)
    except ValueError:
        pass
    else:
        raise AssertionError(
            "ModuleRegistry must reject duplicate module names"
        )


def test_builder_builds_registry():
    module = RecordingModule()

    registry = (
        ModuleBuilder()
        .add(module)
        .build()
    )

    assert registry.modules == [module]


def test_builder_rejects_duplicate_module_names():
    builder = ModuleBuilder()

    builder.add(RecordingModule("Trading"))

    try:
        builder.add(RecordingModule("Trading"))
    except ValueError:
        pass
    else:
        raise AssertionError(
            "ModuleBuilder must reject duplicate module names"
        )


def test_loader_returns_loaded_module():
    loader = ModuleLoader()
    module = RecordingModule()

    loaded = loader.load(module)

    assert loaded is module


def test_manager_starts_modules_in_registration_order():
    manager = ModuleManager()
    events = []

    class OrderedModule(RecordingModule):
        def start(self, context: ModuleContext) -> None:
            events.append(f"{self.name}:start")

    first = OrderedModule("First")
    second = OrderedModule("Second")
    third = OrderedModule("Third")

    manager.add(first)
    manager.add(second)
    manager.add(third)

    context = ModuleContext(ServiceCollection())

    manager.start(context)

    assert events == [
        "First:start",
        "Second:start",
        "Third:start",
    ]


def test_manager_stops_modules_in_reverse_registration_order():
    manager = ModuleManager()
    events = []

    class OrderedModule(RecordingModule):
        def start(self, context: ModuleContext) -> None:
            events.append(f"{self.name}:start")

        def stop(self, context: ModuleContext) -> None:
            events.append(f"{self.name}:stop")

    first = OrderedModule("First")
    second = OrderedModule("Second")
    third = OrderedModule("Third")

    manager.add(first)
    manager.add(second)
    manager.add(third)

    context = ModuleContext(ServiceCollection())

    manager.start(context)
    manager.stop(context)

    assert events == [
        "First:start",
        "Second:start",
        "Third:start",
        "Third:stop",
        "Second:stop",
        "First:stop",
    ]