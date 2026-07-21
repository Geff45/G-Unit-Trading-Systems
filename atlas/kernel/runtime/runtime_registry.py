class RuntimeRegistry:
    
    def __init__(self):

        self._runtimes = {}

    def register(self, runtime):

        self._runtimes[
            runtime.descriptor.runtime_id
        ] = runtime

    def get(self, runtime_id):

        return self._runtimes.get(runtime_id)

    def all(self):

        return list(
            self._runtimes.values()
        )

    def count(self):

        return len(self._runtimes)