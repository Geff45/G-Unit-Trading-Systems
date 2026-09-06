from pathlib import Path
from forge.template_engine import TemplateEngine


class BaseGenerator:

    def __init__(self, project_root="."):
        self.project_root = Path(project_root).resolve()
        self.templates = TemplateEngine()

    def generate(self, *args, **kwargs):
        return None

    def write_file(self, relative_path, content):

        destination = self.project_root / relative_path

        destination.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        destination.write_text(
            content,
            encoding="utf-8"
        )

        return destination