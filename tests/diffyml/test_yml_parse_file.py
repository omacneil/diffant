import tempfile

import pytest

from diffant import exceptions
from diffant.diffyml import DiffYML


def test_parse_file_correct_yaml():
    """Test parsing of correct yaml file."""
    diff_yml = DiffYML()
    with tempfile.NamedTemporaryFile(mode="w+", delete=False) as f:
        f.write("key: value\n")
        f.seek(0)
        data = diff_yml.parse_file(f.name)
    assert isinstance(data, dict), "Parsed data is not a dictionary."
    assert data.get("key") == "value", "Parsed data does not contain expected values."


def test_parse_file_no_keys_yaml():
    """Test parsing of incorrect yaml file."""
    diff_yml = DiffYML()
    with tempfile.NamedTemporaryFile(mode="w+", delete=False) as f:
        incorrect_yaml_content = "bad content no colon so no key\n"
        f.write(incorrect_yaml_content)
        f.seek(0)
        with pytest.raises(exceptions.ParseError) as exc:
            _ = diff_yml.parse_file(f.name)
            print(f"{str(exc)=}")
    assert "failed to parse" in str(exc.value)


def test_parse_file_inconsistant_keys_yaml():
    """Test parsing of inconsistant yaml file."""
    diff_yml = DiffYML()
    with tempfile.NamedTemporaryFile(mode="w+", delete=False) as f:
        incorrect_yaml_content = "animals:\n-dog\n"
        f.write(incorrect_yaml_content)
        f.seek(0)
        with pytest.raises(exceptions.ParseError) as exc:
            _ = diff_yml.parse_file(f.name)
    assert "failed to parse" in str(exc.value)
