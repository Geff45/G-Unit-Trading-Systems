"""
G-Unit Platform

Request Delegate
"""

from __future__ import annotations

from collections.abc import Callable

from .context import MiddlewareContext

RequestDelegate = Callable[[MiddlewareContext], None]