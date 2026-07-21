"""
Atlas Base Manager
"""

from core.base.component import BaseComponent


class BaseManager(BaseComponent):

    def __init__(self, name):

        super().__init__(name)

        self.items = {}

    def register(self, key, item):

        self.items[key] = item

    def remove(self, key):

        self.items.pop(key, None)

    def get(self, key):

        return self.items.get(key)

    def list(self):

        return list(self.items.keys())