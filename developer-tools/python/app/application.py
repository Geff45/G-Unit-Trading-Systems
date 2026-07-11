"""
=============================================================
ATLAS Forge

Application Core

Feature:
    DTF-002
=============================================================
"""

from core.registry import Registry
from services.console import Console
from core.bootstrap import BootstrapEngine


class Application:

    def __init__(self):

        self.registry = Registry()

        self.console = Console()

        self.bootstrap = BootstrapEngine()

        self.registry.register("console", self.console)

        self.registry.register("bootstrap", self.bootstrap)

    def start(self):

        self.console.title("ATLAS Forge")

        self.bootstrap.run()

        self.console.success("Application started successfully.")

        self.console.line()

        self.console.info("Registered Services:")

        for service in self.registry.list():

            self.console.info(f" • {service}")