from kernel.registry.service_registry import ServiceRegistry
from kernel.registry.service_descriptor import ServiceDescriptor

from kernel.events.event_bus import EventBus
from kernel.events.event import Event

from kernel.runtime.container import DependencyContainer


class AtlasRuntime:

    def __init__(self):

        self.registry = ServiceRegistry()

        self.event_bus = EventBus()

        self.container = DependencyContainer()

    def register(self, interface, implementation):

        self.container.register(interface, implementation)

    def resolve(self, interface):

        return self.container.resolve(interface)

    def add_service(
        self,
        descriptor: ServiceDescriptor,
        implementation,
    ):

        self.registry.register(descriptor)

        self.container.register(
            implementation,
            implementation,
        )

        self.event_bus.publish(
            Event(
                event_type="service.registered",
                source=descriptor.service_id,
                payload=descriptor,
            )
        )

    def services(self):

        return self.registry.count()