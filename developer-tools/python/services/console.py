"""
=============================================================
GUTS Developer Toolkit

Console Service

Purpose:
    Centralized console output.

Version:
    0.1.0-alpha
=============================================================
"""

class Console:

    @staticmethod
    def line():

        print("-" * 60)

    @staticmethod
    def title(text):

        Console.line()

        print(text)

        Console.line()

    @staticmethod
    def info(text):

        print(f"[INFO] {text}")

    @staticmethod
    def success(text):

        print(f"[ OK ] {text}")

    @staticmethod
    def warning(text):

        print(f"[WARN] {text}")

    @staticmethod
    def error(text):

        print(f"[FAIL] {text}")