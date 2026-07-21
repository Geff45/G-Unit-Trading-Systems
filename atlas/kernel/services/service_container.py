from kernel.services.service_manager import (
    ServiceManager,
)


class ServiceContainer:
    """
    Global Atlas service container.
    """

    def __init__(self):

        self.manager = ServiceManager()

    def register(self, service):

        self.manager.register(
            service
        )

    def manager_instance(self):

        return self.manager