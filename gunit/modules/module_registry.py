from __future__ import annotations

from gunit.modules.module import Module


class ModuleRegistry:
    """
    Registry of Atlas modules.

    Module names must be unique within the registry.
    """

    def __init__(self) -> None:
        self._modules: list[Module] = []

    def register(self, module: Module) -> None:
        """
        Register a module.

        Raises:
            ValueError: If another module with the same name
                is already registered.
        """
        if any(existing.name == module.name for existing in self._modules):
            raise ValueError(
                f"Module '{module.name}' is already registered"
            )

        self._modules.append(module)

    @property
    def modules(self) -> list[Module]:
        """
        Return a snapshot of the registered modules.

        The returned list is independent from the internal
        registry collection.
        """
        return list(self._modules)
