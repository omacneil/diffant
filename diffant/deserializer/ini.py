"""Ini Deserializer."""
import configparser
from typing import Any, Dict

from diffant import exceptions
from diffant.deserializer.abc import DeserializerABC


class INIDeserializer(DeserializerABC):
    """Ini file content deserializer."""

    def deserialize(self, file_contents: str) -> Dict[str, Any]:
        """Given an ini file, return a dict corresponding to the file contents

        Args:
            file_contents (str): file to parse

        Raises:
            exceptions.DeserializationError: If the configparser library tells us
            we failed to parse

        Returns:
            Dict[str, Any]:  corresponding to the ini file
        """
        config = configparser.ConfigParser()
        try:
            config.read_string(file_contents)
        except configparser.Error as exc:
            raise exceptions.DeserializationError(
                "Failed to deserialize file contents"
            ) from exc

        return {s: dict(config.items(s)) for s in config.sections()}
