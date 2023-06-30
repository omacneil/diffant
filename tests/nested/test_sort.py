"""
    test diffant.nested.sort()
"""

from diffant import nested


def test_nested_sort_with_nested_dict():
    """Test nested.sort function with nested dictionaries in default sorted order."""
    data = {"b": {"c": [4, 2, 6]}, "a": {"d": [3, 1, 5]}, "e": {"f": [9, 7, 8]}}
    expected = {"a": {"d": [1, 3, 5]}, "b": {"c": [2, 4, 6]}, "e": {"f": [7, 8, 9]}}
    assert nested.sort(data) == expected


def test_nested_sort_with_nested_dicts_sorted_descending():
    """Test nested.sort function with nested dictionaries in descending sorted order."""
    data = {"e": {"f": [9, 7, 8]}, "b": {"c": [4, 2, 6]}, "a": {"d": [3, 1, 5]}}
    expected = {"e": {"f": [7, 8, 9]}, "b": {"c": [2, 4, 6]}, "a": {"d": [1, 3, 5]}}
    assert nested.sort(data) == expected


def test_nested_sort_with_nested_dicts_sorted_by_key_length():
    """Test nested.sort function with nested dictionaries sorted by key length."""
    data = {"a": {"d": [3, 1, 5]}, "b": {"c": [4, 2, 6]}, "e": {"f": [9, 7, 8]}}
    expected = {"e": {"f": [7, 8, 9]}, "a": {"d": [1, 3, 5]}, "b": {"c": [2, 4, 6]}}
    assert nested.sort(data) == expected


def test_nested_sort_with_nested_lists():
    """Test nested.sort function with nested lists in default sorted order."""
    data = [[4, 2, [7, 5, 3]], [1, {"b": 6, "a": 8}], ["c", {"d": 9, "e": 7}]]
    expected = [[1, {"a": 8, "b": 6}], [2, 4, [3, 5, 7]], ["c", {"d": 9, "e": 7}]]
    assert nested.sort(data) == expected


def test_nested_sort_with_nested_lists_sorted_descending():
    """Test nested.sort function with nested lists in descending sorted order."""
    data = [["c", {"d": 9, "e": 7}], [1, {"b": 6, "a": 8}], [4, 2, [7, 5, 3]]]
    expected = [[1, {"a": 8, "b": 6}], [2, 4, [3, 5, 7]], ["c", {"d": 9, "e": 7}]]
    assert nested.sort(data) == expected


def test_nested_sort_with_mixed_data():
    """Test nested.sort function with mixed data types in default sorted order."""
    data = [1, {"b": None, "a": 8}, [4, None, 2], None, {"c": 5, "d": None}]
    expected = [1, None, [2, 4, None], {"a": 8, "b": None}, {"c": 5, "d": None}]
    assert nested.sort(data) == expected
