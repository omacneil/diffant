import tempfile

import pytest

from diffant import exceptions
from diffant.deserializer.ini import INIDeserializer


def test_deserialize_file_correct_ini():
    """Test parsing of correct ini file."""
    diff_ini = INIDeserializer()
    with tempfile.NamedTemporaryFile(mode="w+", delete=False) as f:
        f.write("[section]\nkey=value\n")
        f.seek(0)
        data = diff_ini.deserialize(f.read())
    assert isinstance(data, dict), "Parsed data is not a dictionary."
    assert "section" in data, "Parsed data does not contain expected sections."
    assert (
        data["section"].get("key") == "value"
    ), "Parsed data does not contain expected values."


def test_deserialize_file_no_keys_ini():
    """Test parsing of incorrect ini file."""
    diff_ini = INIDeserializer()
    with tempfile.NamedTemporaryFile(mode="w+", delete=False) as f:
        incorrect_ini_content = "bad content no equals so no key\n"
        f.write(incorrect_ini_content)
        f.seek(0)
        with pytest.raises(exceptions.DeserializationError) as exc:
            _ = diff_ini.deserialize(f.read())
    assert "Failed to deserialize" in str(exc.value)


def test_deserialize_file_inconsistant_keys_ini():
    """Test parsing of inconsistant ini file."""
    diff_ini = INIDeserializer()
    with tempfile.NamedTemporaryFile(mode="w+", delete=False) as f:
        incorrect_ini_content = "[animals]\ndog\n"
        f.write(incorrect_ini_content)
        f.seek(0)
        with pytest.raises(exceptions.DeserializationError) as exc:
            _ = diff_ini.deserialize(f.read())
    assert "Failed to deserialize" in str(exc.value)
