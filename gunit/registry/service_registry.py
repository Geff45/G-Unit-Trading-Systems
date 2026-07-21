"""
G-UNIT Platform Kernel

Service Registry

Central discovery system for all platform services.
"""


from typing import Dict, List, Optional

from ..container.service_descriptor import ServiceDescriptor



class ServiceRegistry:
    """
    Stores and discovers platform services.
    """


    def __init__(self):

        self._services: Dict[
            str,
            ServiceDescriptor
        ] = {}



    def register(
        self,
        descriptor: ServiceDescriptor
    ):
        """
        Register service.
        """

        name = descriptor.name


        if name in self._services:

            raise Exception(
                f"Service already exists: {name}"
            )


        self._services[name] = descriptor



    def find(
        self,
        service_name: str
    ) -> Optional[ServiceDescriptor]:
        """
        Find service by name.
        """

        return self._services.get(
            service_name
        )



    def remove(
        self,
        service_name: str
    ):
        """
        Remove service.
        """

        self._services.pop(
            service_name,
            None
        )



    def exists(
        self,
        service_name: str
    ) -> bool:
        """
        Check if service exists.
        """

        return service_name in self._services



    def list_all(self) -> List[str]:
        """
        Return all registered services.
        """

        return list(
            self._services.keys()
        )



    def describe(
        self,
        service_name: str
    ):

        service = self.find(
            service_name
        )


        if not service:
            return None


        return service.info()