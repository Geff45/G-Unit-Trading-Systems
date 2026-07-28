from __future__ import annotations

import sys

from forge.commands import doctor, make, version
from forge.console import Console


def main():

    if len(sys.argv) < 2:
        Console.error("No command specified.")
        return

    command = sys.argv[1].lower()

    if command == "version":
        version()
        return

    if command == "doctor":
        doctor()
        return

    if command == "make":

        if len(sys.argv) < 4:
            Console.error(
                "Usage: forge make module ClassName"
            )
            return

        make(
            sys.argv[2],
            sys.argv[3],
        )
        return

    Console.error(f"Unknown command '{command}'")


if __name__ == "__main__":
    main()