from forge.commands import NewCommand
from forge.framework import CommandContext


def test_new_command_creates_project(tmp_path):

    command = NewCommand()

    context = CommandContext(
        args=["TestProject"],
        working_directory=str(tmp_path),
    )

    result = command.run(context)

    assert result.success is True

    project = tmp_path / "TestProject"

    assert project.exists()
    assert (project / "README.md").exists()
    assert (project / "forge.yaml").exists()
    assert (project / "pyproject.toml").exists()
    assert (project / ".gitignore").exists()

    assert (
        project / "src" / "TestProject" / "__init__.py"
    ).exists()

    assert (
        project / "tests" / "__init__.py"
    ).exists()