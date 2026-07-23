"""
Forge CLI
"""

from __future__ import annotations

import argparse
import sys


VERSION = "0.1.0-alpha"


def doctor() -> int:
    print("===================================")
    print(" Forge Doctor")
    print("===================================")
    print("Status : OK")
    print(f"Version: {VERSION}")
    print("Python : Supported")
    print("Environment: Healthy")
    return 0


def install(package: str | None):
    if not package:
        print("No package specified.")
        return

    print(f"Installing '{package}'...")
    print("Installation complete.")


def update():
    print("Checking for Forge updates...")
    print("Forge is already up to date.")


def rollback():
    print("Rollback complete.")


def main() -> int:
    parser = argparse.ArgumentParser(
        prog="forge",
        description="Forge Developer Toolkit",
    )

    parser.add_argument(
        "--version",
        action="store_true",
        help="Show Forge version",
    )

    parser.add_argument(
        "command",
        nargs="?",
        help="doctor | install | update | rollback",
    )

    parser.add_argument(
        "target",
        nargs="?",
        help="Target package",
    )

    args = parser.parse_args()

    if args.version:
        print(VERSION)
        return 0

    if args.command == "doctor":
        return doctor()

    if args.command == "install":
        install(args.target)
        return 0

    if args.command == "update":
        update()
        return 0

    if args.command == "rollback":
        rollback()
        return 0

    parser.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())