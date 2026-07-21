from kernel.registry.service_descriptor import ServiceDescriptor


class ServiceRegistry:

    def __init__(self):

        self._services = {}

    def register(self, descriptor: ServiceDescriptor):

        if descriptor.service_id in self._services:
            raise ValueError(
                f"Service '{descriptor.service_id}' already registered."
            )

        self._services[descriptor.service_id] = descriptor

    def get(self, service_id: str):

        return self._services.get(service_id)

    def exists(self, service_id: str):

        return service_id in self._services

    def count(self):

        return len(self._services)

    def all_services(self):

        return list(self._services.values())