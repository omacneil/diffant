"""XML Deserializer."""
from typing import Any, Dict
from xml.parsers.expat import ExpatError

import xmltodict

from diffant import exceptions
from diffant.deserializer.abc import DeserializerABC


class XMLDeserializer(DeserializerABC):
    """XML file content deserializer."""

    def deserialize(self, file_contents: str) -> Dict[str, Any]:
        """Given an xml file, return a dict corresponding to the file contents

        Args:
            file_contents (str): file to parse

        Raises:
            exceptions.DeserializationError: If the xmltodict library tells us we failed to parse

        Returns:
            Dict[str, Any]: corresponding to the xml
        """
        try:
            result = xmltodict.parse(file_contents, process_namespaces=True)
        except ExpatError as exc:
            raise exceptions.DeserializationError(
                "Failed to deserialize file contents"
            ) from exc

        return result
