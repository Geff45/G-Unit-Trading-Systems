from __future__ import annotations

from datetime import datetime


class Console:
    """
    Simple console abstraction for Forge.
    """

    @staticmethod
    def write(message: str = ""):
        print(message)

    @staticmethod
    def success(message: str):
        print(f"[OK] {message}")

    @staticmethod
    def warning(message: str):
        print(f"[WARNING] {message}")

    @staticmethod
    def error(message: str):
        print(f"[ERROR] {message}")

    @staticmethod
    def info(message: str):
        print(f"[INFO] {message}")

    @staticmethod
    def banner():

        Console.write("=" * 60)
        Console.write("Forge Developer Toolkit")
        Console.write(f"Started : {datetime.now()}")
        Console.write("=" * 60)