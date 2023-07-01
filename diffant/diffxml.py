""" Contains class to parse xml """

from typing import Any
from xml.parsers.expat import ExpatError, errors

import xmltodict

from diffant import exceptions
from diffant.diffabc import DiffABC


class DiffXML(DiffABC):
    """class to produce the structured diff of xml files."""

    def parse_file(self, file: str) -> Any:
        """Given an xml file, return a dict corresponding to the file contents

        Args:
            file (str): file to parse

        Raises:
            exceptions.ParseError: If the xmltodict library tells us we failed to parse

        Returns:
            Dict[str, Any]: corresponding to the xml
        """
        with open(file, "r", encoding="utf-8") as fh:
            fh_contents = fh.read()
        try:
            result = xmltodict.parse(fh_contents, process_namespaces=True)
        except ExpatError as exc:
            msg = f"failed to parse: '{file}'\n"
            msg += f"line: {exc.lineno} column: {exc.offset}\n"
            # pylint: disable=no-member
            msg += f"error: {str(errors.messages[exc.code])}"
            raise exceptions.ParseError(msg) from exc

        return result
