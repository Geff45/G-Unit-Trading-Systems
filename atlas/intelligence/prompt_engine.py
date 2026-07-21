"""
Atlas Prompt Engine
"""


class PromptEngine:

    def __init__(self):

        self.templates = {}

    def register(self, name, template):

        self.templates[name] = template

    def generate(self, name, **kwargs):

        prompt = self.templates[name]

        return prompt.format(**kwargs)