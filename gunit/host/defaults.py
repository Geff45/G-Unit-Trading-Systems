"""
Host defaults.
"""

from __future__ import annotations

from .options import HostOptions


class HostDefaults:
    """
    Factory for default host configuration.
    """

    @staticmethod
    def create() -> HostOptions:
        """
        Returns the default host options.
        """

        return HostOptions()

    @staticmethod
    def development() -> HostOptions:
        """
        Development configuration.
        """

        return HostOptions(
            environment="Development",
        )

    @staticmethod
    def production() -> HostOptions:
        """
        Production configuration.
        """

        return HostOptions(
            environment="Production",
        )