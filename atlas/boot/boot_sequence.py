import time


class BootSequence:

    def __init__(self):

        self.modules = [

            "Runtime",

            "Configuration",

            "Dependency Container",

            "Event Bus",

            "Cloud",

            "Workers",

            "Distributed Engine",

            "Execution Engine",

            "SDK",

            "Forge",

            "Hub",

            "Intelligence",

            "DataHub",

            "Trading Engine",

            "Scheduler",

            "Monitoring"

        ]

    def run(self):

        for module in self.modules:

            print(f"Loading {module}...")

            time.sleep(0.1)

            print(f"{module} Ready")