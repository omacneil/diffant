"""Reader abstract base class."""
from abc import ABC, abstractmethod


class ReaderABC(ABC):
    """Abstract base class for Readers."""

    @abstractmethod
    def read_file(self, file_path: str) -> str:
        """ "Read the file contents into a string."""
