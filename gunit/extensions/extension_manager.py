from .extension_registry import ExtensionRegistry


class ExtensionManager:

    def __init__(self):
        self.registry = ExtensionRegistry()

    # -------------------------
    # Registration
    # -------------------------

    def register(self, extension):
        self.registry.register(extension)

    def unregister(self, name):
        self.registry.unregister(name)

    # Backwards compatibility

    def load(self, extension):
        self.register(extension)

    def unload(self, name):
        self.unregister(name)

    # -------------------------
    # Lookup
    # -------------------------

    def get(self, name):
        return self.registry.get(name)

    def all(self):
        return self.registry.all()

    def clear(self):
        self.registry.clear()

    # -------------------------
    # Lifecycle
    # -------------------------

    def initialize(self, name):
        extension = self.get(name)
        if extension:
            extension.initialize()

    def enable(self, name):
        extension = self.get(name)
        if extension:
            extension.enable()

    def disable(self, name):
        extension = self.get(name)
        if extension:
            extension.disable()


__all__ = ["ExtensionManager"]
