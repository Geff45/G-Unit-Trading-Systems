from pathlib import Path
import importlib

from generator import Generator


ROOT = Path(__file__).resolve().parent.parent


def run_phase(number):

    phase = f"tools.phases.phase{number:02d}"

    module = importlib.import_module(phase)

    generator = Generator(ROOT)

    module.run(generator)


if __name__ == "__main__":

    import argparse

    parser = argparse.ArgumentParser()

    parser.add_argument("phase", type=int)

    args = parser.parse_args()

    run_phase(args.phase)