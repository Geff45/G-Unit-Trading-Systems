"""
Dependency Resolver.
"""

from __future__ import annotations

from typing import Any


class DependencyResolver:
    """
    Resolves dependencies from the service container.
    """

    def __init__(self, container: Any) -> None:
        self._container = container

    def resolve(self, service_type: type) -> Any:
        return self._container.resolve(service_type)

    def resolve_all(self, service_types: list[type]) -> list[Any]:
        resolved: list[Any] = []

        for service in service_types:
            resolved.append(self.resolve(service))

        return resolved

    def dependency_graph(self) -> list[str]:
        """
        Placeholder for future dependency graph generation.
        """

        resolved: list[str] = []
        visited: set[str] = set()

        for service in getattr(self._container, "_services", {}):
            name = str(service)

            if name not in visited:
                visited.add(name)
                resolved.append(name)

        return resolved