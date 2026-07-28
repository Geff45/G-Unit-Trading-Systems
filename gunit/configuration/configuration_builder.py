from .configuration import Configuration


class ConfigurationBuilder:

    def __init__(self):
        self._configuration = Configuration()

    def add(self, key, value):
        self._configuration.set(key, value)
        return self

    def build(self):
        return self._configuration


__all__ = ["ConfigurationBuilder"]
