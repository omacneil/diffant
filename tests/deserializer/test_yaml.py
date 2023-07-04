import tempfile

import pytest

from diffant import exceptions
from diffant.deserializer.yaml import YAMLDeserializer


def test_deserialize_file_correct_yaml():
    """Test parsing of correct yaml file."""
    diff_yml = YAMLDeserializer()
    with tempfile.NamedTemporaryFile(mode="w+", delete=False) as f:
        f.write("key: value\n")
        f.seek(0)
        data = diff_yml.deserialize(f.read())
    assert isinstance(data, dict), "Parsed data is not a dictionary."
    assert data.get("key") == "value", "Parsed data does not contain expected values."


def test_deserialize_file_no_keys_yaml():
    """Test parsing of incorrect yaml file."""
    diff_yml = YAMLDeserializer()
    with tempfile.NamedTemporaryFile(mode="w+", delete=False) as f:
        incorrect_yaml_content = "bad content no colon so no key\n"
        f.write(incorrect_yaml_content)
        f.seek(0)
        with pytest.raises(exceptions.DeserializationError) as exc:
            _ = diff_yml.deserialize(f.read())
            print(f"{str(exc)=}")
    assert "Deserialized type is not a dict" in str(exc.value)


def test_deserialize_file_inconsistant_keys_yaml():
    """Test parsing of inconsistant yaml file."""
    diff_yml = YAMLDeserializer()
    with tempfile.NamedTemporaryFile(mode="w+", delete=False) as f:
        incorrect_yaml_content = "animals:\n-dog\n"
        f.write(incorrect_yaml_content)
        f.seek(0)
        with pytest.raises(exceptions.DeserializationError) as exc:
            _ = diff_yml.deserialize(f.read())
    assert "Failed to deserialize" in str(exc.value)
