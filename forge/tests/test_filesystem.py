from pathlib import Path

from forge.filesystem import project_root


def test_project_root_returns_path():
    root = project_root()

    assert isinstance(root, Path)
    assert root.exists()
    assert root.is_dir()


def test_project_root_points_to_project():
    root = project_root()

    assert root.name == "G-Unit-Trading-Systems"