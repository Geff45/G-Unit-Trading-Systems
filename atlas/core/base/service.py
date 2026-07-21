"""
Atlas Base Service
"""

from core.base.component import BaseComponent


class BaseService(BaseComponent):

    def __init__(self, name):

        super().__init__(name)

        self.dependencies = []

    def add_dependency(self, dependency):

        self.dependencies.append(dependency)

    def list_dependencies(self):

        return self.dependencies