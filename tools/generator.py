"""
G-UNIT Generator

Creates folders and files from templates.
"""

from __future__ import annotations

from pathlib import Path


class Generator:

    def __init__(self, root: Path):

        self.root = Path(root)

    def mkdir(self, path: str):

        (self.root / path).mkdir(parents=True, exist_ok=True)

    def write(self, path: str, content: str):

        file = self.root / path

        file.parent.mkdir(parents=True, exist_ok=True)

        file.write_text(content.strip() + "\n", encoding="utf-8")

    def append(self, path: str, content: str):

        file = self.root / path

        file.parent.mkdir(parents=True, exist_ok=True)

        with file.open("a", encoding="utf-8") as f:

            f.write(content)

    def replace(self, path: str, old: str, new: str):

        file = self.root / path

        text = file.read_text(encoding="utf-8")

        text = text.replace(old, new)

        file.write_text(text, encoding="utf-8")

    def exists(self, path: str):

        return (self.root / path).exists()