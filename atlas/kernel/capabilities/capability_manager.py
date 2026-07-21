from kernel.capabilities.capability_registry import (
    CapabilityRegistry,
)

from kernel.capabilities.capability_state import (
    CapabilityState,
)


class CapabilityManager:
    """
    Atlas Enterprise Capability Manager.
    """

    def __init__(self):

        self.registry = CapabilityRegistry()

    def register(self, capability):

        self.registry.register(capability)

    def initialize(self, capability_id):

        capability = self.registry.get(capability_id)

        capability.initialize()

        capability.descriptor.state = (
            CapabilityState.INITIALIZED
        )

    def activate(self, capability_id):

        capability = self.registry.get(capability_id)

        capability.activate()

        capability.descriptor.state = (
            CapabilityState.ACTIVE
        )

    def pause(self, capability_id):

        capability = self.registry.get(capability_id)

        capability.pause()

        capability.descriptor.state = (
            CapabilityState.PAUSED
        )

    def shutdown(self, capability_id):

        capability = self.registry.get(capability_id)

        capability.shutdown()

        capability.descriptor.state = (
            CapabilityState.SHUTDOWN
        )