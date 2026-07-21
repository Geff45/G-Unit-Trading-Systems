"""
Atlas Forge Template Engine

Loads templates from disk and renders them
using simple placeholder substitution.

Version: 2.0.0
"""

from __future__ import annotations

from pathlib import Path
from typing import Dict


class TemplateEngine:
    """
    Loads and renders template files.
    """

    def __init__(self, template_directory: Path):

        self._template_directory = Path(template_directory)

    def template_exists(self, template_name: str) -> bool:

        return self._get_template_file(template_name).exists()

    def render(
        self,
        template_name: str,
        variables: Dict[str, str] | None = None,
    ) -> str:

        template_file = self._get_template_file(template_name)

        if not template_file.exists():
            raise FileNotFoundError(
                f"Template not found: {template_name}"
            )

        content = template_file.read_text(
            encoding="utf-8"
        )

        if variables:

            for key, value in variables.items():

                placeholder = "{{" + key + "}}"

                content = content.replace(
                    placeholder,
                    str(value)
                )

        return content

    def _get_template_file(
        self,
        template_name: str
    ) -> Path:

        return self._template_directory / f"{template_name}.tpl"