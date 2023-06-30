"""
tests  for method _get_config_files
"""
import os
import tempfile

import pytest

from diffant.diffjson import DiffJson

# pylint: disable=protected-access


def test_get_config_files():
    """
    Test the get_config_files method
    """
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_dir_path = os.path.abspath(temp_dir)
        for filename in ("file1.json", "file2.json", "file3.txt"):
            with open(f"{temp_dir_path}/{filename}", "w+", encoding="utf8") as fh:
                fh.write("some text")
        differ = DiffJson()
        differ._files_type = "json"
        differ._config_dir = temp_dir_path
        differ._get_config_files()

        expected_files = [f"{temp_dir_path}/file1.json", f"{temp_dir_path}/file2.json"]
        assert differ._config_files == expected_files


def test_gjff_no_json_files_there():
    """
    test we throw FileNotFound when there aren't any json files in the dir
    """
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_dir_path = os.path.abspath(temp_dir)
        with pytest.raises(FileNotFoundError) as excinfo:
            differ = DiffJson()
            differ._config_dir = temp_dir_path
            differ._get_config_files()
            assert str(excinfo.value) == "No JSON files found in the directory"
