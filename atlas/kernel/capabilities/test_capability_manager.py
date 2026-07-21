from kernel.capabilities.capability import Capability

from kernel.capabilities.capability_descriptor import (
    CapabilityDescriptor,
)

from kernel.capabilities.capability_loader import (
    CapabilityLoader,
)


class EconomicCalendarCapability(Capability):

    def initialize(self):

        print("Calendar Initialized")

    def activate(self):

        print("Calendar Active")

    def pause(self):

        print("Calendar Paused")

    def shutdown(self):

        print("Calendar Shutdown")


descriptor = CapabilityDescriptor(
    capability_id="calendar",

    name="Economic Calendar",

    version="1.0.0",

    plugin="fundamental_plugin",

    description="High-impact economic events",
)

capability = EconomicCalendarCapability(
    descriptor
)

loader = CapabilityLoader()

manager = loader.load_capabilities(
    [capability]
)

print()

print("Capabilities Registered:")

print(manager.registry.count())

print()

manager.initialize("calendar")

manager.activate("calendar")

print()

print(capability.descriptor.state.value)