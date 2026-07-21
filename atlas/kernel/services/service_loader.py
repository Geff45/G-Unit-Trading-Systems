from kernel.services.service_container import (
    ServiceContainer,
)


class ServiceLoader:
    """
    Responsible for loading
    Atlas services during boot.
    """

    def __init__(self):

        self.container = ServiceContainer()

    def load(
        self,
        services,
    ):

        for service in services:

            self.container.register(
                service
            )

        return self.container