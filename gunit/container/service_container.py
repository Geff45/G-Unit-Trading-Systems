"""
G-UNIT Platform Kernel

Service Container

Central dependency injection container.
"""

from typing import Dict, Any, Type

from .service_descriptor import ServiceDescriptor



class ServiceContainer:
    """
    Dependency Injection container.

    Responsible for registering,
    resolving and managing services.
    """


    def __init__(self):

        self._descriptors: Dict[str, ServiceDescriptor] = {}

        self._instances: Dict[str, Any] = {}



    def register(
        self,
        descriptor: ServiceDescriptor
    ):
        """
        Register a service descriptor.
        """

        identity = descriptor.name

        if identity in self._descriptors:
            raise Exception(
                f"Service already registered: {identity}"
            )


        self._descriptors[identity] = descriptor



    def resolve(
        self,
        name: str
    ):
        """
        Resolve a service instance.
        """


        if name in self._instances:
            return self._instances[name]


        if name not in self._descriptors:
            raise Exception(
                f"Service not found: {name}"
            )


        descriptor = self._descriptors[name]


        module = __import__(
            descriptor.module,
            fromlist=[descriptor.service_class]
        )


        service_class = getattr(
            module,
            descriptor.service_class
        )


        instance = service_class()


        self._instances[name] = instance


        return instance



    def remove(
        self,
        name: str
    ):
        """
        Remove service.
        """

        self._descriptors.pop(
            name,
            None
        )


        self._instances.pop(
            name,
            None
        )



    def list_services(self):
        """
        Return registered services.
        """

        return list(
            self._descriptors.keys()
        )