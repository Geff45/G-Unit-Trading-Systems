from forge.scaffold import ProjectScaffold


def test_project_scaffold(tmp_path):

    project = tmp_path / "TestProject"

    scaffold = ProjectScaffold(project)

    result = scaffold.create()

    assert result == project

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