def run(g):
    
    g.mkdir("gunit/core/runtime")

    g.write(
        "gunit/core/runtime/__init__.py",
        """
from .runtime import Runtime
"""
    )

    g.write(
        "gunit/core/runtime/runtime.py",
        """
class Runtime:

    pass
"""
    )