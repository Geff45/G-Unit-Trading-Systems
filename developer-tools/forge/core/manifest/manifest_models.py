"""
Atlas Forge Manifest Models

Strongly typed models used by the manifest loader.

Version: 1.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List


@dataclass(slots=True)
class DirectoryEntry:
    path: str
    required: bool = True
    description: str = ""


@dataclass(slots=True)
class FileEntry:
    path: str
    template: str = ""
    category: str = ""
    version: str = "1.0.0"
    required: bool = True
    description: str = ""
    action: str = "create"
    depends_on: List[str] = field(default_factory=list)


@dataclass(slots=True)
class Manifest:
    manifest_version: str
    forge_version: str
    directories: List[DirectoryEntry]
    files: List[FileEntry]