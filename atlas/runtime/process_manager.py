class ProcessManager:

    def __init__(self):
        self.processes = {}

    def start(self, name):
        self.processes[name] = "running"
        return {
            "process": name,
            "status": "running"
        }

    def stop(self, name):
        self.processes[name] = "stopped"
        return {
            "process": name,
            "status": "stopped"
        }

    def status(self, name):
        return self.processes.get(name, "unknown")

    def list(self):
        return self.processes