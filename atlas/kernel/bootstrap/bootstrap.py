from kernel.runtime.runtime import AtlasRuntime


class AtlasBootstrap:

    """
    Responsible for building and initializing the Atlas kernel.
    """

    def __init__(self):
        self.runtime = AtlasRuntime()

    def boot(self):

        print("Booting Atlas...")

        print("Loading Runtime...")

        print("Kernel Ready")

        return self.runtime