from boot.boot_sequence import BootSequence


class BootManager:

    def __init__(self):
        self.sequence = BootSequence()

    def boot(self):
        print("=" * 60)
        print("           ATLAS AI OPERATING SYSTEM")
        print("=" * 60)

        self.sequence.run()

        print("=" * 60)
        print("Atlas Boot Complete")
        print("=" * 60)