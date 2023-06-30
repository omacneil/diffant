"""test main.create_differ() """
import pytest

from diffant import exceptions
from diffant.main import create_differ


class MockDiffClass:
    pass


def test_create_differ_supported_type():
    mapping = {"txt": MockDiffClass}
    file_type = "txt"
    diff = create_differ(mapping, file_type)
    assert isinstance(diff, MockDiffClass)


def test_create_differ_unsupported_type():
    mapping = {"txt": MockDiffClass}
    file_type = "pdf"
    with pytest.raises(exceptions.InputDirContentsError) as excinfo:
        create_differ(mapping, file_type)
    assert str(excinfo.value) == "unspported file type: 'pdf'\nsupported types: txt"


def test_create_differ_no_mapping():
    mapping = {}
    file_type = "txt"
    with pytest.raises(exceptions.InputDirContentsError) as excinfo:
        create_differ(mapping, file_type)
    assert str(excinfo.value) == "unspported file type: 'txt'\nsupported types: "
