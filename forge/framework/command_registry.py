class CommandRegistry:
    """
    Central registry for Forge commands.
    """

    def __init__(self):
        self._commands = {}

    def register(self, command):
        """
        Register a command instance.
        """

        self._commands[command.name] = command


    def get(self, name):
        """
        Retrieve command by name.
        """

        return self._commands.get(name)


    def remove(self, name):
        """
        Remove command.
        """

        if name in self._commands:
            del self._commands[name]


    def exists(self, name):
        """
        Check command existence.
        """

        return name in self._commands


    def list_commands(self):
        """
        Return registered commands.
        """

        return list(self._commands.keys())
