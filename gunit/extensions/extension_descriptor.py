from dataclasses import dataclass


@dataclass
class ExtensionDescriptor:
    name: str
    version: str
    author: str
    description: str


__all__ = ["ExtensionDescriptor"]
