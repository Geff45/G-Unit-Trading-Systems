import sys

from forge.cli.router import CLIRouter
from forge.commands import (
    VersionCommand,
    DoctorCommand,
    MakeCommand,
    NewCommand,
)
from forge.framework import CommandContext, CommandRegistry


VERSION = "1.0"


def build_registry():
    registry = CommandRegistry()

    registry.register(VersionCommand())
    registry.register(DoctorCommand())
    registry.register(MakeCommand())
    registry.register(NewCommand())

    return registry


def print_help():
    print(
        """
Forge CLI

Usage:
    python -m forge <command> [arguments]

Commands:
    version                 Show Forge version
    doctor                  Check Forge system health
    new <project_name>      Create a new project
    make <type> <name>      Generate a component

Options:
    --help, -h              Show this help message
    --version               Show Forge version

Examples:
    python -m forge version
    python -m forge doctor
    python -m forge new MyProject
    python -m forge make module TradeEngine
"""
    )


def main(args=None):

    if args is None:
        args = sys.argv[1:]

    if not args:
        print_help()
        return 0

    if args[0] in ("--help", "-h"):
        print_help()
        return 0

    if args[0] == "--version":
        print(f"Forge Version {VERSION}")
        return 0

    registry = build_registry()

    router = CLIRouter(registry)

    context = CommandContext(
        args=args[1:],
        options={},
    )

    result = router.route(
        args,
        context,
    )

    if result is None:
        return 1

    if result.message:
        print(result.message)

    if result.data:
        if isinstance(result.data, dict):
            for key, value in result.data.items():
                print(f"{key}: {value}")
        else:
            print(result.data)

    return 0 if result.success else 1


if __name__ == "__main__":
    raise SystemExit(main())
