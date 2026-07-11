"""
Bootstrap Engine
"""

from pathlib import Path

from core.manifest import ManifestEngine
from services.console import Console


class BootstrapEngine:

    def __init__(self):

        self.project_root = Path(__file__).resolve().parents[3]

    def run(self):

        Console.title("BOOTSTRAP")

        manifest = ManifestEngine(self.project_root)

        manifest.load()

        project = manifest.project()

        Console.info(f"Project : {project['name']}")

        Console.info(f"Version : {project['version']}")

        Console.info(f"Platform: {project['platform']}")

        Console.info(f"Engine  : {project['engine']}")

        Console.success("Bootstrap completed successfully.")