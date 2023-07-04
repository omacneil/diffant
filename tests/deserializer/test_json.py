"""JSON deserializer tests."""
import json
import tempfile

import pytest

from diffant import exceptions
from diffant.deserializer.json import JSONDeserializer


def test_deserialize_json_bad_file():
    """see if we throw an exception given a file with bad jason"""
    with tempfile.NamedTemporaryFile(mode="w+", suffix=".json") as temp_file1:
        temp_file1.write("garbage")
        temp_file1.seek(0)
        with pytest.raises(exceptions.DeserializationError):
            differ = JSONDeserializer()
            differ.deserialize(temp_file1.read())
