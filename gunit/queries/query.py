"""
Base Query.
"""

from __future__ import annotations

from abc import ABC


class Query(ABC):
    """
    Base class for all queries.

    Queries never modify state.
    They only request data.
    """

    pass