from gunit.commands.command import Command


class BuildCommand(Command):
    pass


def test_command_name():

    command = BuildCommand()

    assert command.name == "BuildCommand"