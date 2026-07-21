"""
Atlas AI Operating System
=========================

AtlasObject

Universal base object for the Atlas platform.
"""

from __future__ import annotations

from common.identity.identity import Identity
from common.identity.identity_types import IdentityType
from common.lifecycle.lifecycle_manager import LifecycleManager


class AtlasObject:

    def __init__(
        self,
        name: str,
        category: IdentityType,
        version: str = "1.0.0"
    ):

        self._identity = Identity.create(
            name=name,
            category=category,
            version=version
        )

        self._lifecycle = LifecycleManager()

    # -----------------------------------
    # Identity
    # -----------------------------------

    @property
    def identity(self):

        return self._identity

    @property
    def uid(self):

        return self._identity.uid

    @property
    def name(self):

        return self._identity.name

    @property
    def version(self):

        return self._identity.version

    # -----------------------------------
    # Lifecycle
    # -----------------------------------

    @property
    def lifecycle(self):

        return self._lifecycle

    @property
    def state(self):

        return self._lifecycle.current()

    # -----------------------------------
    # Information
    # -----------------------------------

    def info(self):

        return {

            "id": self.uid,

            "name": self.name,

            "version": self.version,

            "state": self.state.name,

            "category": self.identity.category.value
        }