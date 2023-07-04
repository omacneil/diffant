"""JSON deserializer."""
import json
from typing import Any, Dict

from diffant import exceptions
from diffant.deserializer.abc import DeserializerABC


class JSONDeserializer(DeserializerABC):
    """JSON file content deserializer."""

    def deserialize(self, file_contents: str) -> Dict[str, Any]:
        """Given a json file, return a dict corresponding to the file contents

        Args:
            file_contents (str): file to parse

        Raises:
            exceptions.DeserializationError: If the json library tells us we failed to parse

        Returns:
            Dict[str, Any]:  corresponding to the json
        """
        try:
            result = json.loads(file_contents)
        except json.decoder.JSONDecodeError as exc:
            raise exceptions.DeserializationError(
                "Failed to deserialize file contents"
            ) from exc

        return result
