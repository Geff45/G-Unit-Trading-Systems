import json

from .configuration_provider import ConfigurationProvider


class JsonProvider(ConfigurationProvider):

    def load_file(self, path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)


__all__ = ["JsonProvider"]
