from kernel.services.service import Service
from kernel.services.service_state import ServiceState


class ServiceManager:
    """
    Atlas Enterprise Service Manager

    Responsible for registering and managing
    all services running inside Atlas.
    """

    def __init__(self):

        self._services = {}

    def register(
        self,
        service: Service,
    ):

        self._services[
            service.descriptor.service_id
        ] = service

    def get(
        self,
        service_id: str,
    ):

        return self._services.get(
            service_id
        )

    def exists(
        self,
        service_id: str,
    ):

        return service_id in self._services

    def services(self):

        return list(
            self._services.values()
        )

    def descriptors(self):

        return [
            service.descriptor
            for service in self._services.values()
        ]

    def count(self):

        return len(
            self._services
        )

    def start(
        self,
        service_id: str,
    ):

        service = self.get(
            service_id
        )

        if service is None:

            raise ValueError(
                f"{service_id} not registered."
            )

        service.start()

        service.descriptor.state = (
            ServiceState.RUNNING
        )

    def stop(
        self,
        service_id: str,
    ):

        service = self.get(
            service_id
        )

        if service is None:

            raise ValueError(
                f"{service_id} not registered."
            )

        service.stop()

        service.descriptor.state = (
            ServiceState.STOPPED
        )

    def pause(
        self,
        service_id: str,
    ):

        service = self.get(
            service_id
        )

        if service is None:

            raise ValueError(
                f"{service_id} not registered."
            )

        service.pause()

        service.descriptor.state = (
            ServiceState.PAUSED
        )

    def resume(
        self,
        service_id: str,
    ):

        service = self.get(
            service_id
        )

        if service is None:

            raise ValueError(
                f"{service_id} not registered."
            )

        service.resume()

        service.descriptor.state = (
            ServiceState.RUNNING
        )