from kernel.capabilities.capability_manager import (
    CapabilityManager,
)


class CapabilityLoader:
    """
    Loads Atlas capabilities.
    """

    def __init__(self):

        self.manager = CapabilityManager()

    def load_capabilities(
        self,
        capabilities,
    ):

        for capability in capabilities:

            self.manager.register(capability)

        return self.manager