"""
G-UNIT Platform Kernel

Service Descriptor

Defines metadata and lifecycle information
for every registered service.
"""

from dataclasses import dataclass, field
from typing import List, Dict, Optional


@dataclass
class ServiceDescriptor:
    """
    Defines a G-UNIT service.

    Every platform component must have
    a descriptor before registration.
    """

    name: str

    version: str

    module: str

    service_class: str


    dependencies: List[str] = field(
        default_factory=list
    )


    configuration: Dict = field(
        default_factory=dict
    )


    metadata: Dict = field(
        default_factory=dict
    )


    enabled: bool = True


    lifecycle: str = "managed"


    description: Optional[str] = None



    def identity(self) -> str:
        """
        Returns unique service identity.
        """

        return f"{self.name}:{self.version}"



    def requires(self) -> List[str]:
        """
        Returns required dependencies.
        """

        return self.dependencies



    def info(self) -> Dict:
        """
        Returns service information.
        """

        return {

            "name": self.name,

            "version": self.version,

            "module": self.module,

            "class": self.service_class,

            "dependencies": self.dependencies,

            "enabled": self.enabled,

            "lifecycle": self.lifecycle

        }