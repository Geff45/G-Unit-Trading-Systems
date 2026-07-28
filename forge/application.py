from __future__ import annotations

from forge.commands.doctor import DoctorCommand


class ForgeApplication:
    """
    Main Forge application.

    Responsible for registering and executing commands.
    """

    def __init__(self):

        self.commands = {}

        self.register("doctor", DoctorCommand())

    def register(self, name, command):

        self.commands[name] = command

    def has_command(self, name):

        return name in self.commands

    def command_names(self):

        return sorted(self.commands.keys())

    def execute(self, name):

        if name not in self.commands:
            raise ValueError(f"Unknown command '{name}'")

        self.commands[name].run()