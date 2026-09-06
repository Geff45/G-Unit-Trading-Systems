class ForgeApplication:

    def __init__(self):
        self.commands = {}

    def register(self, name, command):
        self.commands[name] = command

    def execute(self, name, *args):
        return self.commands[name](*args)

    def has_command(self, name):
        return name in self.commands

    def command_names(self):
        return sorted(self.commands.keys())
