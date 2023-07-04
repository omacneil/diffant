"""Reader abstract base class."""
from cloudpathlib import CloudPath

from diffant import exceptions
from diffant.reader.abc import ReaderABC


class CloudReader(ReaderABC):
    """Abstract base class for Readers."""

    def read_file(self, file_path: str) -> str:
        """ "Read the file contents into a string."""
        try:
            contents = CloudPath(file_path).read_text()  # type: ignore [abstract]
        except Exception as exc:
            raise exceptions.ReadError("Failed to read file contents") from exc
        return contents
