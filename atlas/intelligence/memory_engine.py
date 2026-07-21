"""
Atlas Memory Engine
"""


class MemoryEngine:

    def __init__(self):

        self.memory = {}

    def remember(self, key, value):

        self.memory[key] = value

    def recall(self, key):

        return self.memory.get(key)

    def forget(self, key):

        self.memory.pop(key, None)

    def clear(self):

        self.memory.clear()