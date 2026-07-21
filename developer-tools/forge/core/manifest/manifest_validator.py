"""
Atlas Forge Manifest Validator

Performs validation of structure.json.

Version: 1.0.0
"""

from __future__ import annotations

from .manifest_models import Manifest


class ManifestValidator:

    def validate(self, manifest: Manifest) -> None:

        if not manifest.manifest_version:
            raise ValueError(
                "Manifest version missing."
            )

        if not manifest.forge_version:
            raise ValueError(
                "Forge version missing."
            )

        paths = set()

        for directory in manifest.directories:

            if directory.path in paths:
                raise ValueError(
                    f"Duplicate directory: {directory.path}"
                )

            paths.add(directory.path)

        for file in manifest.files:

            if file.path in paths:
                raise ValueError(
                    f"Duplicate file: {file.path}"
                )

            paths.add(file.path)