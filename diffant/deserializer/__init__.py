"""Deserializer module."""
from diffant.exceptions import DeserializationError

from .ini import INIDeserializer
from .json import JSONDeserializer
from .xml import XMLDeserializer
from .yaml import YAMLDeserializer


def deserialize(file_contents: str, suffix: str):
    """Deserialize a string to a dict."""
    if "json" in suffix:
        return JSONDeserializer().deserialize(file_contents)
    elif "ini" in suffix:
        return INIDeserializer().deserialize(file_contents)
    elif "yaml" in suffix:
        return YAMLDeserializer().deserialize(file_contents)
    elif "xml" in suffix:
        return XMLDeserializer().deserialize(file_contents)
    else:
        raise DeserializationError(f"Unsupported file type: {suffix}")
