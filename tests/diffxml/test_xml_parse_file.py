import tempfile

import pytest

from diffant import exceptions
from diffant.diffxml import DiffXML


def test_parse_file_correct_xml():
    """Test parsing of correct XML file."""
    diff_xml = DiffXML()
    with tempfile.NamedTemporaryFile(mode="w+", delete=False) as f:
        f.write("<root><key>value</key></root>")
        f.seek(0)
        data = diff_xml.parse_file(f.name)
    assert isinstance(data, dict), "Parsed data is not a dictionary."
    assert (
        data["root"]["key"] == "value"
    ), "Parsed data does not contain expected values."


def test_parse_file_no_closing_tag_xml():
    """Test parsing of incorrect XML file."""
    diff_xml = DiffXML()
    with tempfile.NamedTemporaryFile(mode="w+", delete=False) as f:
        incorrect_xml_content = "<root><key>value"
        f.write(incorrect_xml_content)
        f.seek(0)
        with pytest.raises(exceptions.ParseError) as exc:
            _ = diff_xml.parse_file(f.name)
    assert "failed to parse" in str(exc.value)
    assert "no element found" in str(exc.value)


def test_parse_file_inconsistent_tag_xml():
    """Test parsing of inconsistent XML file."""
    diff_xml = DiffXML()
    with tempfile.NamedTemporaryFile(mode="w+", delete=False) as f:
        incorrect_xml_content = "<root><key>value</keys></root>"
        f.write(incorrect_xml_content)
        f.seek(0)
        with pytest.raises(exceptions.ParseError) as exc:
            _ = diff_xml.parse_file(f.name)
    assert "failed to parse" in str(exc.value)
    assert "mismatched tag" in str(exc.value)
