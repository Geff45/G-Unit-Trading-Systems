from pathlib import Path

from forge.framework import Command, CommandResult
from forge.scaffold import ProjectScaffold


class NewCommand(Command):

    name = "new"

    def execute(self, context):

        if not context.args:
            return CommandResult.fail(
                "Usage: forge new <project_name>"
            )

        project_name = context.args[0]

        project_root = (
            Path(context.working_directory)
            / project_name
        )

        if project_root.exists():
            return CommandResult.fail(
                f"Project already exists: {project_name}"
            )

        scaffold = ProjectScaffold(project_root)

        scaffold.create()

        return CommandResult.ok(
            f"Project created: {project_name}",
            {
                "project": str(project_root),
            },
        )