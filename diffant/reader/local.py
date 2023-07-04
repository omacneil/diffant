"""Reader abstract base class."""
from pathlib import Path

from diffant import exceptions
from diffant.reader.abc import ReaderABC


class LocalReader(ReaderABC):
    """Abstract base class for Readers."""

    def read_file(self, file_path: str) -> str:
        """ "Read the file contents into a string."""
        try:
            contents = Path(file_path).read_text()
        except Exception as exc:
            raise exceptions.ReadError("Failed to read file contents") from exc
        return contents
