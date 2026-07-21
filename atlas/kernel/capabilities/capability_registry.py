from kernel.capabilities.capability import Capability


class CapabilityRegistry:
    """
    Stores every Atlas capability.
    """

    def __init__(self):

        self._capabilities = {}

    def register(
        self,
        capability: Capability,
    ):

        self._capabilities[
            capability.descriptor.capability_id
        ] = capability

    def get(
        self,
        capability_id: str,
    ):

        return self._capabilities.get(
            capability_id
        )

    def exists(
        self,
        capability_id: str,
    ):

        return capability_id in self._capabilities

    def all(self):

        return list(
            self._capabilities.values()
        )

    def count(self):

        return len(
            self._capabilities
        )