"""
Atlas Forge Database Models

Defines the core data models used by the Project Database Service.

Version: 1.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime


@dataclass(slots=True)
class ProjectModel:
    name: str
    version: str
    description: str = ""
    author: str = ""
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)


@dataclass(slots=True)
class ModuleModel:
    name: str
    path: str
    enabled: bool = True
    version: str = "1.0.0"


@dataclass(slots=True)
class DependencyModel:
    source: str
    target: str
    dependency_type: str = "runtime"


@dataclass(slots=True)
class SnapshotModel:
    id: str
    timestamp: datetime = field(default_factory=datetime.utcnow)
    description: str = ""


@dataclass(slots=True)
class HistoryModel:
    timestamp: datetime = field(default_factory=datetime.utcnow)
    action: str = ""
    user: str = "system"