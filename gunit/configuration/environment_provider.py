import os

from .configuration_provider import ConfigurationProvider


class EnvironmentProvider(ConfigurationProvider):

    def load(self):
        return dict(os.environ)


__all__ = ["EnvironmentProvider"]
