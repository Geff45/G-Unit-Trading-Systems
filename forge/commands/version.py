from forge.console import Console
from forge import __version__


def execute():
    """
    Display the installed Forge version.
    """
    Console.banner()
    Console.success(f"Forge Version {__version__}")