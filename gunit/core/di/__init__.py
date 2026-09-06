"""
Enterprise Dependency Injection Framework.

This package provides:

- ServiceCollection
- ServiceProvider
- ServiceScope
- ServiceDescriptor
- ServiceLifetime
"""

from .lifetime import ServiceLifetime
from .descriptor import ServiceDescriptor
from .collection import ServiceCollection
from .provider import ServiceProvider, ServiceScope

__all__ = [
    "ServiceLifetime",
    "ServiceDescriptor",
    "ServiceCollection",
    "ServiceProvider",
    "ServiceScope",
]
