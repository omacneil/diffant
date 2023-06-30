import pytest

from diffant.diffjson import DiffJson

# pylint: disable=protected-access


@pytest.fixture
def sample_data():
    """
    Fixture that returns sample data for testing.
    """
    return {
        "root:sub_key:sub_sub_key": {
            "values": {
                "red": ["f01.json", "f02.json"],
                "purple": ["f04.json", "f05.json"],
                "/*MISSING*/": ["/path/to/file/no_key.json"],
            }
        },
        "root:sub:": {
            "values": {
                "zeus": ["f01.json", "f02.json", "f03.json", "f04.json", "f05.json"]
            }
        },
    }


def test_remove_no_diff_from_flat_recs(sample_data):
    """
    Test for remove_no_diff_from_flat_recs method.

    Args:
        sample_data: Sample data for testing.

    """
    # Call the method
    differ = DiffJson()
    differ._flat_recs = sample_data
    differ._remove_no_diff_from_flat_recs()

    # Verify the result
    assert len(differ._flat_recs) == 1
    assert "root:sub_key:sub_sub_key" in differ._flat_recs
    assert "root:sub:" not in differ._flat_recs

    values = differ._flat_recs["root:sub_key:sub_sub_key"]["values"]
    assert len(values) == 3
    assert "red" in values
    assert "purple" in values
    assert "/*MISSING*/" in values


def test_remove_no_diff_from_flat_recs_empty_dict():
    """
    Test for remove_no_diff_from_flat_recs method with an empty dictionary.
    """
    # Call the method with an empty dictionary
    differ = DiffJson()
    differ._flat_recs = {}
    differ._remove_no_diff_from_flat_recs()

    # Verify the result
    assert len(differ._flat_recs) == 0


def test_remove_no_diff_from_flat_recs_no_single_value():
    """
    Test for remove_no_diff_from_flat_recs method with a dictionary that doesn't have
    any single-value entries.
    """
    # Call the method with a dictionary that doesn't have any single-value entries
    data = {
        "key1": {"values": {"value1": ["file1.json", "file2.json"]}},
        "key2": {"values": {"value2": ["file3.json", "file4.json"]}},
        "key3": {"values": {"value3": ["file5.json", "file6.json"]}},
    }
    differ = DiffJson()
    differ._flat_recs = data
    differ._remove_no_diff_from_flat_recs()
    # Verify the result
    assert len(differ._flat_recs) == 0
