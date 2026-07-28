from abc import ABC, abstractmethod
from pathlib import Path

from forge.template_engine import TemplateEngine


class BaseGenerator(ABC):
    """
    Base class for all Forge generators.
    """

    def __init__(self, project_root="."):
        self.project_root = Path(project_root).resolve()
        self.templates = TemplateEngine()

    @abstractmethod
    def generate(self, *args, **kwargs):
        """
        Generate project artifacts.
        """
        raise NotImplementedError()

    def write_file(self, relative_path: str, content: str):
        """
        Writes generated content to disk.
        """

        destination = self.project_root / relative_path

        destination.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        destination.write_text(
            content,
            encoding="utf-8",
        )

        return destination