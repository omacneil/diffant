"""YAML Deserializer."""
from typing import Any

import yaml

from diffant import exceptions
from diffant.deserializer.abc import DeserializerABC


class YAMLDeserializer(DeserializerABC):
    """YAML file content deserializer."""

    def deserialize(self, file_contents: str) -> Any:
        """Given a yaml file, return a dict corresponding to the file contents

        Args:
            file_contents (str): file to parse

        Raises:
            exceptions.DeserializationError: If the yaml library tells us we failed to parse

        Returns:
            Dict[str, Any]:  corresponding to the yaml
        """
        try:
            result = yaml.safe_load(file_contents)
        except yaml.YAMLError as exc:
            raise exceptions.DeserializationError(
                "Failed to deserialize file contents"
            ) from exc

        if not isinstance(result, dict):
            raise exceptions.DeserializationError(
                f"Deserialized type is not a dict but instead a {type(result)}"
            )

        return result
