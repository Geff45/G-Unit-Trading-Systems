"""
Configuration schema definitions.
"""

from __future__ import annotations

from pydantic import BaseModel


class SystemConfig(BaseModel):
    name: str
    version: str
    mode: str


class LoggingConfig(BaseModel):
    level: str
    file: str


class WorkspaceConfig(BaseModel):
    root: str


class KernelConfig(BaseModel):
    auto_boot: bool


class SecurityConfig(BaseModel):
    telemetry: bool


class Configuration(BaseModel):
    system: SystemConfig
    logging: LoggingConfig
    workspace: WorkspaceConfig
    kernel: KernelConfig
    security: SecurityConfig
    