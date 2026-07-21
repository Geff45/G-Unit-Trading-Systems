"""
G-UNIT Platform Kernel

Capability Registry

Manages intelligence domains and platform abilities.
"""


from typing import Dict, List, Optional



class CapabilityDescriptor:
    """
    Defines a platform capability.
    """


    def __init__(
        self,
        name: str,
        version: str,
        provider: str,
        description: str = "",
        services: List[str] = None
    ):

        self.name = name

        self.version = version

        self.provider = provider

        self.description = description

        self.services = services or []



    def info(self):

        return {

            "name": self.name,

            "version": self.version,

            "provider": self.provider,

            "description": self.description,

            "services": self.services

        }



class CapabilityRegistry:
    """
    Stores and discovers platform capabilities.
    """


    def __init__(self):

        self._capabilities: Dict[
            str,
            CapabilityDescriptor
        ] = {}



    def register(
        self,
        capability: CapabilityDescriptor
    ):

        name = capability.name


        if name in self._capabilities:

            raise Exception(
                f"Capability already registered: {name}"
            )


        self._capabilities[name] = capability



    def find(
        self,
        name: str
    ) -> Optional[CapabilityDescriptor]:

        return self._capabilities.get(
            name
        )



    def exists(
        self,
        name: str
    ) -> bool:

        return name in self._capabilities



    def list_all(self):

        return list(
            self._capabilities.keys()
        )



    def describe(
        self,
        name: str
    ):

        capability = self.find(name)


        if not capability:

            return None


        return capability.info()