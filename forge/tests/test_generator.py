from pathlib import Path
import tempfile

from forge.generators import BaseGenerator


def test_write_file():

    with tempfile.TemporaryDirectory() as tmp:

        generator = BaseGenerator(tmp)

        file = Path(tmp) / "hello.txt"

        generator.write_file(
            file,
            "Hello Forge",
        )

        assert file.exists()

        assert file.read_text() == "Hello Forge"