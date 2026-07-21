"""
Atlas Forge CLI Application

Version: 2.0.0
"""

from .parser import Parser
from .dispatcher import Dispatcher
from .registry import CommandRegistry

from .commands.help_command import HelpCommand
from .commands.version_command import VersionCommand
from .commands.doctor_command import DoctorCommand
from .commands.new_command import NewCommand
from .commands.build_command import BuildCommand
from .commands.clean_command import CleanCommand
from .commands.install_command import InstallCommand
from .commands.plugin_command import PluginCommand


class CLIApplication:

    def __init__(self):

        self.registry = CommandRegistry()

        self.registry.register(HelpCommand())
        self.registry.register(VersionCommand())
        self.registry.register(DoctorCommand())
        self.registry.register(NewCommand())
        self.registry.register(BuildCommand())
        self.registry.register(CleanCommand())
        self.registry.register(InstallCommand())
        self.registry.register(PluginCommand())

        self.dispatcher = Dispatcher(self.registry)

    def run(self):

        parser = Parser()

        command, arguments = parser.parse()

        self.dispatcher.dispatch(command, arguments)