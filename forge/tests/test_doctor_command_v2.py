from forge.commands import DoctorCommand
from forge.framework import CommandContext


def test_doctor_command():

    command = DoctorCommand()

    result = command.run(
        CommandContext()
    )

    assert result.success
    assert isinstance(result.data, dict)
