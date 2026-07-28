from .configuration_provider import ConfigurationProvider


class MemoryProvider(ConfigurationProvider):

    def __init__(self):
        self._values = {}

    def load(self):
        return self._values

    def add(self, key, value):
        self._values[key] = value


__all__ = ["MemoryProvider"]
