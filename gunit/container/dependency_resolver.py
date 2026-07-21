"""
G-UNIT Platform Kernel

Dependency Resolver

Responsible for analysing service
dependencies and resolving startup order.
"""


from typing import Dict, List

from .service_descriptor import ServiceDescriptor



class DependencyResolver:
    """
    Resolves dependencies between services.
    """


    def __init__(self):

        self.services: Dict[str, ServiceDescriptor] = {}



    def register(
        self,
        descriptor: ServiceDescriptor
    ):
        """
        Add service descriptor.
        """

        self.services[
            descriptor.name
        ] = descriptor



    def resolve(
        self,
        service_name: str
    ) -> List[str]:
        """
        Return ordered dependency list.
        """

        if service_name not in self.services:
            raise Exception(
                f"Unknown service: {service_name}"
            )


        resolved = []

        visited = set()

        self._resolve_recursive(
            service_name,
            visited,
            resolved
        )


        return resolved



    def _resolve_recursive(
        self,
        name,
        visited,
        resolved
    ):

        if name in visited:
            return


        visited.add(name)


        service = self.services[name]


        for dependency in service.dependencies:

            if dependency not in self.services:

                raise Exception(
                    f"Missing dependency: {dependency}"
                )


            self._resolve_recursive(
                dependency,
                visited,
                resolved
            )


        resolved.append(name)



    def dependency_tree(
        self
    ):
        """
        Return complete dependency map.
        """

        tree = {}


        for name, service in self.services.items():

            tree[name] = service.dependencies


        return tree