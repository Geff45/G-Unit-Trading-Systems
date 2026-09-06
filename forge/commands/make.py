from pathlib import Path

from forge.commands.make_command import MakeCommand
from forge.framework import CommandContext


def execute(*args):
    """
    Execute the make command from the current working directory.

    This helper is primarily used by the public Forge command API
    and by tests that change the process working directory.
    """

    return MakeCommand().run(
        CommandContext(
            args=list(args),
            working_directory=str(Path.cwd()),
        )
    )


__all__ = [
    "MakeCommand",
    "execute",
]