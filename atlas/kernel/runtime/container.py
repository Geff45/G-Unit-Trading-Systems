from kernel.runtime.registration import ServiceRegistration
from kernel.runtime.lifetime import ServiceLifetime


class DependencyContainer:

    def __init__(self):

        self._registrations = {}

    def register(
        self,
        interface,
        implementation,
        lifetime=ServiceLifetime.SINGLETON,
    ):

        self._registrations[interface] = ServiceRegistration(
            interface,
            implementation,
            lifetime,
        )

    def resolve(self, interface):

        registration = self._registrations[interface]

        if registration.lifetime == ServiceLifetime.SINGLETON:

            if registration.instance is None:
                registration.instance = registration.implementation()

            return registration.instance

        return registration.implementation()