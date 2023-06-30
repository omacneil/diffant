"""
test method create_flat_key_recs
"""
from diffant.diffjson import DiffJson

# pylint: disable=protected-access


def test_create_flat_key_recs_empty_input():
    """
    When the method is called with empty list
    Then the method should set an empty dictionary
    """
    diff_json = DiffJson()
    diff_json._parsed_file_recs = []
    diff_json._create_flat_recs()
    assert not diff_json._flat_recs


def test_create_flat_key_recs_with_data():
    """
    Given a list of records with filename and parsed_contents
    When the method is called with the records
    Then the result should be a dictionary with each unique flattened key and its
    corresponding list of values and filenames
    """
    diff_json = DiffJson()
    diff_json._parsed_file_recs = [
        {
            "filename": "path/to/file1",
            "parsed_content": {"key1": "value1", "key2": "value2"},
        },
        {
            "filename": "path/to/file2",
            "parsed_content": {"key1": "value1", "key3": "value3"},
        },
    ]
    diff_json._create_flat_recs()

    expected_result = {
        "key1:": {"values": {"value1": ["path/to/file1", "path/to/file2"]}},
        "key2:": {"values": {"value2": ["path/to/file1"]}},
        "key3:": {"values": {"value3": ["path/to/file2"]}},
    }

    assert diff_json._flat_recs == expected_result


def test_create_flat_key_recs_with_complex_data():
    """
    Given a list of records with complex parsed_contents
    When the method is called with the records. Then the result
    should be a dictionary with each unique flattened key and its
    corresponding list of values and filenames
    """
    diff_json = DiffJson()
    diff_json._parsed_file_recs = [
        {
            "filename": "path/to/file1",
            "parsed_content": {"key1": {"sub_key1": "value1"}, "key2": "value2"},
        },
        {
            "filename": "path/to/file2",
            "parsed_content": {"key1": {"sub_key1": "value3"}, "key3": "value3"},
        },
    ]

    diff_json._create_flat_recs()

    expected_result = {
        "key1:sub_key1:": {
            "values": {"value1": ["path/to/file1"], "value3": ["path/to/file2"]}
        },
        "key2:": {"values": {"value2": ["path/to/file1"]}},
        "key3:": {"values": {"value3": ["path/to/file2"]}},
    }

    assert diff_json._flat_recs == expected_result
