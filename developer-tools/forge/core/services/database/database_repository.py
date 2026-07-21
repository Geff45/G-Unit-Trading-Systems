"""
Atlas Forge Database Repository

Provides JSON persistence for project metadata.

Version: 1.0.0
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


class DatabaseRepository:

    def __init__(self, database_directory: Path) -> None:

        self._database_directory = database_directory

        self._database_directory.mkdir(
            parents=True,
            exist_ok=True
        )

    def _file(self, filename: str) -> Path:

        return self._database_directory / filename

    def load(self, filename: str) -> dict[str, Any]:

        file = self._file(filename)

        if not file.exists():
            return {}

        with file.open(
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(f)

    def save(
        self,
        filename: str,
        data: dict[str, Any]
    ) -> None:

        file = self._file(filename)

        with file.open(
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                data,
                f,
                indent=4,
                ensure_ascii=False
            )

    def exists(self, filename: str) -> bool:

        return self._file(filename).exists()

    def delete(self, filename: str) -> None:

        file = self._file(filename)

        if file.exists():
            file.unlink()