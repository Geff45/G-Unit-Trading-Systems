from dataclasses import dataclass


@dataclass(slots=True)
class PluginDescriptor:
    name: str
    version: str
    author: str = ""
    description: str = ""