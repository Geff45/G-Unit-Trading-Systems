"""
Atlas Forge Project Generator

Version: 1.0.0
"""

from pathlib import Path

from ..manifest import Manifest
from .generation_report import GenerationReport


class ProjectGenerator:

    def __init__(self):

        self.report = GenerationReport()

    def generate(self, manifest: Manifest):

        for directory in manifest.directories:

            path = Path(directory.path)

            if path.exists():

                self.report.directories_existing += 1

            else:

                path.mkdir(
                    parents=True,
                    exist_ok=True
                )

                self.report.directories_created += 1

        for file in manifest.files:

            path = Path(file.path)

            if path.exists():

                self.report.files_existing += 1

            else:

                path.parent.mkdir(
                    parents=True,
                    exist_ok=True
                )

                path.touch()

                self.report.files_created += 1

        return self.report