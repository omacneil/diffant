import pytest

from diffant.diffjson import DiffJson

# pylint: disable=protected-access


@pytest.fixture
def flat_recs():
    """Fixture that returns a sample flat_recs dictionary."""
    return {
        "root:sub_key:sub_sub_key": {
            "values": {
                "red": ["/path/to/file01.json", "/path/to/jfile02.json"],
                "purple": ["/path/to/file04.json", "/path/to/jfile05.json"],
            }
        }
    }


def test_add_missing_keys_to_flat_recs_missing_key(flat_recs):
    """Test case for add_missing_keys_to_flat_recs method with a missing key."""
    files = ["/path/to/file/no_key.json"]
    expected_result = {
        "root:sub_key:sub_sub_key": {
            "values": {
                "red": ["/path/to/file01.json", "/path/to/jfile02.json"],
                "purple": ["/path/to/file04.json", "/path/to/jfile05.json"],
                "/*MISSING*/": ["/path/to/file/no_key.json"],
            }
        }
    }
    differ = DiffJson()
    differ._config_files = files
    differ._flat_recs = flat_recs
    differ._add_missing_keys_to_flat_recs()
    assert differ._flat_recs == expected_result


def test_add_missing_keys_to_flat_recs(flat_recs):
    """Test case for add_missing_keys_to_flat_recs method with an existing key."""
    files = ["/path/to/file01.json"]
    expected_result = {
        "root:sub_key:sub_sub_key": {
            "values": {
                "red": ["/path/to/file01.json", "/path/to/jfile02.json"],
                "purple": ["/path/to/file04.json", "/path/to/jfile05.json"],
            }
        }
    }
    differ = DiffJson()
    differ._config_files = files
    differ._flat_recs = flat_recs
    differ._add_missing_keys_to_flat_recs()
    assert differ._flat_recs == expected_result


def test_add_missing_keys_to_flat_recs_multiple_files(flat_recs):
    """Test case for add_missing_keys_to_flat_recs method with multiple files."""
    files = ["/path/to/file01.json", "/path/to/file/no_key.json"]
    expected_result = {
        "root:sub_key:sub_sub_key": {
            "values": {
                "red": ["/path/to/file01.json", "/path/to/jfile02.json"],
                "purple": ["/path/to/file04.json", "/path/to/jfile05.json"],
                "/*MISSING*/": ["/path/to/file/no_key.json"],
            }
        }
    }
    differ = DiffJson()
    differ._config_files = files
    differ._flat_recs = flat_recs
    differ._add_missing_keys_to_flat_recs()
    assert differ._flat_recs == expected_result


def test_add_missing_keys_to_flat_recs_in_more_than_one_file(flat_recs):
    """Test case for add_missing_keys_to_flat_recs method with multiple files."""
    files = ["/path/to/file01.json", "/path/to/file/no_key.json", "file_33.json"]
    expected_result = {
        "root:sub_key:sub_sub_key": {
            "values": {
                "red": ["/path/to/file01.json", "/path/to/jfile02.json"],
                "purple": ["/path/to/file04.json", "/path/to/jfile05.json"],
                "/*MISSING*/": ["/path/to/file/no_key.json", "file_33.json"],
            }
        }
    }
    differ = DiffJson()
    differ._config_files = files
    differ._flat_recs = flat_recs
    differ._add_missing_keys_to_flat_recs()
    assert differ._flat_recs == expected_result
