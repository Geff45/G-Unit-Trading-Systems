class ExtensionRegistry:

    def __init__(self):
        self._extensions = {}

    def register(self, extension):
        name = extension.descriptor.name

        if name in self._extensions:
            raise ValueError(f"Extension '{name}' already registered.")

        self._extensions[name] = extension

    def unregister(self, name):
        self._extensions.pop(name, None)

    def get(self, name):
        return self._extensions.get(name)

    def all(self):
        return list(self._extensions.values())

    def clear(self):
        self._extensions.clear()


__all__ = ["ExtensionRegistry"]
