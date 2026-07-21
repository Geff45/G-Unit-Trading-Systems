"""
Atlas Forge Application

Version: 2.0.0
"""

from __future__ import annotations

from ..bootstrap.bootstrap import Bootstrap


class AtlasApplication:
    """
    Main Atlas Forge application.
    """

    def __init__(self):

        bootstrap = Bootstrap()

        self.engine = bootstrap.create_engine()

    def run(self):

        self.engine.initialize()

        self.engine.start()

        report = self.engine.report()

        print()
        print("=" * 50)
        print("        ATLAS FORGE")
        print("=" * 50)
        print(f"Version              : {report.version}")
        print(f"Engine State         : {report.state}")
        print(f"Registered Services  : {report.registered_services}")
        print(f"Running Services     : {report.running_services}")
        print(f"Failed Services      : {report.failed_services}")
        print("=" * 50)

    def shutdown(self):

        self.engine.stop()

        self.engine.shutdown()