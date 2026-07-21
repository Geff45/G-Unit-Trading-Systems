from configuration import RuntimeConfiguration
from process_manager import ProcessManager
from dependency_manager import DependencyManager
from event_dispatcher import EventDispatcher
from health_monitor import HealthMonitor
from service_loader import ServiceLoader


class RuntimeManager:

    def __init__(self):

        self.config = RuntimeConfiguration()

        self.processes = ProcessManager()

        self.dependencies = DependencyManager()

        self.events = EventDispatcher()

        self.health = HealthMonitor()

        self.loader = ServiceLoader()

    def start(self):

        return {
            "runtime": "Atlas Runtime",
            "status": "started"
        }

    def stop(self):

        return {
            "runtime": "Atlas Runtime",
            "status": "stopped"
        }