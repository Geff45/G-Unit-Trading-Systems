from dataclasses import dataclass

from gunit.di import ServiceCollection


@dataclass(slots=True)
class PluginContext:
    services: ServiceCollection