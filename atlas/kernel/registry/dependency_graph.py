from collections import defaultdict


class DependencyGraph:

    def __init__(self):
        self._graph = defaultdict(set)

    def add_dependency(self, service: str, dependency: str):
        self._graph[service].add(dependency)

    def dependencies_of(self, service: str):
        return list(self._graph.get(service, []))

    def services(self):
        return list(self._graph.keys())

    def has_dependency(self, service: str, dependency: str):
        return dependency in self._graph.get(service, set())