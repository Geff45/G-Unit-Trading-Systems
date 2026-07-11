"""
=============================================================
ATLAS Forge

Registry Service

Feature:
    DTF-002

Purpose:
    Registers shared services and components.
=============================================================
"""

class Registry:

    def __init__(self):

        self._services = {}

    def register(self, name, service):

        self._services[name] = service

    def get(self, name):

        return self._services.get(name)

    def exists(self, name):

        return name in self._services

    def list(self):

        return list(self._services.keys())