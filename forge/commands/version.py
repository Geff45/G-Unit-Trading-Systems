from forge.commands.version_command import VersionCommand


def execute():

    return VersionCommand().execute({})


__all__ = [
    "VersionCommand",
]
