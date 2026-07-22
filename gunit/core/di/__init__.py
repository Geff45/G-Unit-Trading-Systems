"""
Enterprise Dependency Injection Framework.

This package provides:

- ServiceCollection
- ServiceProvider
- ServiceDescriptor
- ServiceLifetime
"""

from .lifetime import ServiceLifetime
from .descriptor import ServiceDescriptor
from .collection import ServiceCollection
from .provider import ServiceProvider

__all__ = [
    "ServiceLifetime",
    "ServiceDescriptor",
    "ServiceCollection",
    "ServiceProvider",
]