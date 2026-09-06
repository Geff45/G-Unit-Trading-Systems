from dataclasses import dataclass


@dataclass(frozen=True)
class ProjectLayout:
    project_root: str

    @property
    def src_dir(self):
        return f"{self.project_root}/src"

    @property
    def tests_dir(self):
        return f"{self.project_root}/tests"

    @property
    def package_dir(self):
        return f"{self.src_dir}/{self.project_root}"