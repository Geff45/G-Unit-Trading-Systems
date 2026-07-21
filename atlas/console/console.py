from console.commands import CommandManager
from console.banner import show_banner


class AtlasConsole:

    def __init__(self):
        self.commands = CommandManager()

    def start(self):

        show_banner()

        while True:

            command = input("\nAtlas> ")

            if command.lower() in ["exit", "quit"]:

                print("\nStopping Atlas...\n")

                break

            print(self.commands.execute(command))