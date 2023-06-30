"""
    tests for flat_items
"""
# pylint: disable=protected-access
from diffant.diffjson import DiffJson


def test_flat_items_nested_dict():
    """Test case for flattening a nested dictionary."""
    data = {
        "appearance": {"color": "red", "shape": "square"},
        "digits": {"0": 0, "1": 3, "2": 22},
    }
    diff_json = DiffJson()
    keys, values = diff_json._flatten_item("", data)
    assert keys == [
        "appearance:color:",
        "appearance:shape:",
        "digits:0:",
        "digits:1:",
        "digits:2:",
    ]
    assert values == ["red", "square", "0", "3", "22"]


def test_flat_items_list_with_dicts():
    """Test case for flattening a list with dictionaries."""
    data = [{"name": "John", "age": 25}, {"name": "Jane", "age": 30}]

    diff_json = DiffJson()
    keys, values = diff_json._flatten_item("", data)
    assert keys == ["0:age:", "0:name:", "1:age:", "1:name:"]
    assert values == ["25", "John", "30", "Jane"]


def test_flat_items_list_with_3_dicts_starting_reverse_sorted():
    """test case for flatting 3 dicts sorted in reverse order"""
    data = [
        {"name": "Jane", "age": 30},
        {"name": "John", "age": 25},
        {"name": "Bob", "age": 12},
    ]
    diff_json = DiffJson()
    keys, values = diff_json._flatten_item("", data)
    assert keys == ["0:age:", "0:name:", "1:age:", "1:name:", "2:age:", "2:name:"]
    assert values == ["12", "Bob", "25", "John", "30", "Jane"]


def test_flat_items_list_with_4_dicts_check_dict_sort_1st_key():
    """test a list with 4 dicts"""
    data = [
        {"name": "Jane", "age": 30},
        {"name": "John", "age": 25},
        {"name": "Bob", "age": 100},
        {"name": "Alex", "age": 60},
    ]
    diff_json = DiffJson()
    keys, values = diff_json._flatten_item("", data)
    assert keys == [
        "0:age:",
        "0:name:",
        "1:age:",
        "1:name:",
        "2:age:",
        "2:name:",
        "3:age:",
        "3:name:",
    ]
    assert values == ["100", "Bob", "25", "John", "30", "Jane", "60", "Alex"]


def test_flat_items_list_with_3_dicts_2():
    """test list with 3 different dicts"""
    data = [
        {"name": "John", "age": 25},
        {"name": "Jane", "age": 30},
        {"name": "Bob", "age": 100},
    ]
    diff_json = DiffJson()
    keys, values = diff_json._flatten_item("", data)
    assert keys == ["0:age:", "0:name:", "1:age:", "1:name:", "2:age:", "2:name:"]
    assert values == ["100", "Bob", "25", "John", "30", "Jane"]


def test_flat_items_unsupported_type():
    """Test case for an unsupported data type."""
    data = set([1, 2, 3])
    diff_json = DiffJson()
    keys, values = diff_json._flatten_item("", data)
    assert keys == ["parse error:{1, 2, 3}"]
    assert values == ["type: <class 'set'>"]


def test_flat_items_empty_dict():
    """Test case for an empty dictionary."""
    data = {}
    diff_json = DiffJson()
    keys, values = diff_json._flatten_item("", data)
    assert not keys
    assert not values


def test_flat_items_empty_list():
    """Test case for an empty list."""
    data = []
    diff_json = DiffJson()
    keys, values = diff_json._flatten_item("", data)
    assert not keys
    assert not values


def test_flat_items_mixed_data_types():
    """Test case for a mixture of data types in a dictionary."""
    data = {
        "name": "John",
        "age": 25,
        "scores": [90, 95, 87],
        "is_active": True,
        "metadata": {"category": "A", "tags": ["tag1", "tag2"]},
    }
    diff_json = DiffJson()
    keys, values = diff_json._flatten_item("", data)
    assert keys == [
        "age:",
        "is_active:",
        "metadata:category:",
        "metadata:tags:0:",
        "metadata:tags:1:",
        "name:",
        "scores:0:",
        "scores:1:",
        "scores:2:",
    ]
    assert values == ["25", "True", "A", "tag1", "tag2", "John", "87", "90", "95"]


def test_flat_items_simple_mixed_data_types():
    """Test case for a mixture of data types in a dictionary."""
    data = {
        "age": 25,
        "scores": [90, 95, 87],
        "is_active": True,
    }
    diff_json = DiffJson()
    keys, values = diff_json._flatten_item("", data)
    assert keys == [
        "age:",
        "is_active:",
        "scores:0:",
        "scores:1:",
        "scores:2:",
    ]
    assert values == ["25", "True", "87", "90", "95"]


def test_flat_items_very_simple_mixed_data_types():
    """Test case for a mixture of data types in a dictionary."""
    data = {"scores": [90, 87]}

    diff_json = DiffJson()
    keys, values = diff_json._flatten_item("", data)
    assert keys == ["scores:0:", "scores:1:"]
    assert values == ["87", "90"]


def test_flat_items_simple_nested_list():
    """Test case for a nested list."""
    data = [1, [2]]
    diff_json = DiffJson()
    keys, values = diff_json._flatten_item("", data)
    assert keys == ["0:", "1:0:"]
    assert values == ["1", "2"]


def test_flat_items_nested_list():
    """Test case for a nested list."""
    data = [1, 2, [3, 4, [5, 6]]]
    diff_json = DiffJson()
    keys, values = diff_json._flatten_item("", data)
    assert keys == ["0:", "1:", "2:0:", "2:1:", "2:2:0:", "2:2:1:"]
    assert values == ["1", "2", "3", "4", "5", "6"]
