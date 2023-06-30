""" test DiffJsona._parse_config_files() """
# pylint: disable=protected-access

import json
import tempfile

import pytest

from diffant import exceptions
from diffant.diffjson import DiffJson


def test_parse_config_files():
    """create some temporary json files and see if we can parse them"""
    # Create temporary JSON files
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json") as temp_file1:
        json_content1 = {"name": "John", "age": 30}
        json.dump(json_content1, temp_file1)
        temp_file1.flush()

        with tempfile.NamedTemporaryFile(mode="w", suffix=".json") as temp_file2:
            json_content2 = {"name": "Jane", "age": 25}
            json.dump(json_content2, temp_file2)
            temp_file2.flush()

            files = [temp_file1.name, temp_file2.name]
            differ = DiffJson()
            differ._config_files = files
            differ._parse_config_files()

        # Check the results
        assert len(differ._parsed_file_recs) == 2

        assert differ._parsed_file_recs[0]["filename"] == temp_file1.name
        assert differ._parsed_file_recs[0]["parsed_content"] == json_content1

        assert differ._parsed_file_recs[1]["filename"] == temp_file2.name
        assert differ._parsed_file_recs[1]["parsed_content"] == json_content2


def test_parse_json_bad_file():
    """see if we throw an exception given a file with bad jason"""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json") as temp_file1:
        temp_file1.write("garbage")
        temp_file1.flush()
        with pytest.raises(exceptions.ParseError) as exc:
            differ = DiffJson()
            _ = differ.parse_file(temp_file1.name)
            assert "failed to parse" in str(exc.value)
