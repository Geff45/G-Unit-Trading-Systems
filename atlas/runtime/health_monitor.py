class HealthMonitor:

    def __init__(self):
        self.components = {}

    def update(self, component, status):

        self.components[component] = status

        return {
            "component": component,
            "status": status
        }

    def report(self):

        healthy = all(
            state == "healthy"
            for state in self.components.values()
        )

        return {
            "overall": "healthy" if healthy else "warning",
            "components": self.components
        }