from .configuration import Configuration


class ConfigurationManager(Configuration):

    def __init__(self, root=None):
        if root is None:
            super().__init__()
            return

        self._data = dict(root.items())

    def get_root(self):
        return self


__all__ = ["ConfigurationManager"]
