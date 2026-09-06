from .configuration import Configuration
from .configuration_root import ConfigurationRoot


class ConfigurationBuilder:

    def __init__(self):
        self._configuration = Configuration()
        self._sources = []

    def add(self, key, value):
        self._configuration.set(key, value)
        return self

    def add_source(self, source):
        self._sources.append(source)
        return self

    def build(self):
        providers = [
            source.build()
            for source in self._sources
        ]

        root = ConfigurationRoot(
            providers=providers
        )

        for key, value in self._configuration.items():
            root.set(key, value)

        return root


__all__ = ["ConfigurationBuilder"]
