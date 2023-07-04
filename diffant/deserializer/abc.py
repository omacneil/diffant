"""Deserializer abstract base class."""
from abc import ABC, abstractmethod
from typing import Any, Dict


class DeserializerABC(ABC):
    """Abstract base class for deserializers."""

    @abstractmethod
    def deserialize(self, file_contents: str) -> Dict[str, Any]:
        """Deserialise the file contents into a dict.

        Args:
            file_contents (str): file to parse

        Raises:
            exceptions.DeserializationError: If we fail to deserialize file contents

        Returns:
            Dict[str, Any]:  corresponding to the file
        """
