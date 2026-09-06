from pathlib import Path


class ProjectScaffold:

    def __init__(self, project_root):
        self.project_root = Path(project_root)

    def create_directories(self):
        package_name = self.project_root.name

        directories = [
            self.project_root / "src" / package_name,
            self.project_root / "tests",
        ]

        for directory in directories:
            directory.mkdir(
                parents=True,
                exist_ok=True,
            )

    def create_files(self):
        package_name = self.project_root.name

        files = {
            "README.md": f"# {package_name}\n",
            "forge.yaml": f"name: {package_name}\nversion: 0.1.0\n",
            "pyproject.toml": (
                "[build-system]\n"
                'requires = ["setuptools>=61"]\n'
                'build-backend = "setuptools.build_meta"\n'
            ),
            ".gitignore": (
                ".venv/\n"
                "__pycache__/\n"
                ".pytest_cache/\n"
            ),
            f"src/{package_name}/__init__.py": "",
            "tests/__init__.py": "",
        }

        for relative_path, content in files.items():
            path = self.project_root / relative_path
            path.parent.mkdir(
                parents=True,
                exist_ok=True,
            )
            path.write_text(
                content,
                encoding="utf-8",
            )

    def create(self):
        self.create_directories()
        self.create_files()

        return self.project_root