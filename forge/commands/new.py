from forge.commands.new_command import NewCommand


def execute():

    return NewCommand().execute({})


__all__ = [
    "NewCommand",
]
