from forge.commands.doctor_command import DoctorCommand
from forge.framework import CommandContext


def execute():
    return DoctorCommand().run(
        CommandContext()
    )