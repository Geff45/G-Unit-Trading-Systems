"""
Atlas Forge Entry Point

Version: 2.0.0
"""

from forge.cli.application import CLIApplication
from forge.core.engine.application import AtlasApplication


def main():

    cli = CLIApplication()

    command, _ = cli.dispatcher.registry.names(), None

    import sys

    if len(sys.argv) > 1:

        cli.run()

    else:

        app = AtlasApplication()

        app.run()


if __name__ == "__main__":

    main()