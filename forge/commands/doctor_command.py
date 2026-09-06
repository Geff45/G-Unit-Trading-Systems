from pathlib import Path
import os

from forge.framework import Command, CommandResult


class DoctorCommand(Command):

    name = "doctor"

    def virtual_environment(self):
        return "VIRTUAL_ENV" in os.environ

    def git_repository(self, path):
        return (Path(path) / ".git").exists()

    def execute(self, context):

        project_root = Path(context.working_directory)

        data = {
            "virtual_environment": self.virtual_environment(),
            "git_repository": self.git_repository(project_root),
        }

        return CommandResult.success_result(
            "Forge system healthy",
            data,
        )
