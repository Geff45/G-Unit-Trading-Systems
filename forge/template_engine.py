from pathlib import Path
from typing import Dict


class TemplateEngine:
    """
    Forge Template Engine

    Loads a template from forge/templates
    and replaces {{VARIABLE}} placeholders.
    """

    def __init__(self, template_directory=None):
        if template_directory is None:
            template_directory = (
                Path(__file__).parent / "templates"
            )

        self.template_directory = Path(template_directory)

    def load(self, template_name: str) -> str:
        """
        Load template contents.
        """

        template = self.template_directory / template_name

        if not template.exists():
            raise FileNotFoundError(
                f"Template '{template_name}' not found."
            )

        return template.read_text(
            encoding="utf-8"
        )

    def render(
        self,
        template_name: str,
        context: Dict[str, str],
    ) -> str:
        """
        Render template using context.
        """

        text = self.load(template_name)

        for key, value in context.items():
            text = text.replace(
                "{{" + key + "}}",
                str(value),
            )

        return text