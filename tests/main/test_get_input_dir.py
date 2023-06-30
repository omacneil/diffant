"""
tests for main.get_input_dir()
"""

import os
import sys
import tempfile

import pytest

from diffant.main import get_input_dir


def test_gid_good_input():
    """create temp dir , pass it in , should succeed"""
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_dir_path = os.path.abspath(temp_dir)
        sys.argv = ["test_script.py", temp_dir_path]
        assert get_input_dir() == temp_dir_path


def test_gid_missing_directory_parameter():
    """case for missing input directory"""
    # reset argv from past tests
    sys.argv = ["test_script.py"]
    # argparse throws sys.exit on bad input
    with pytest.raises(SystemExit):
        get_input_dir()


def test_gid_directory_doesnt_exist():
    """non-existing input directory"""
    sys.argv = ["test_script.py", "doesnt_exist.txt"]

    with pytest.raises(FileNotFoundError):
        get_input_dir()


def test_gid_dir_param_not_a_directory():
    """input directory not being a directory"""
    with tempfile.TemporaryDirectory() as temp_dir:
        with tempfile.NamedTemporaryFile(dir=temp_dir) as temp_file:
            sys.argv = ["test_script.py", temp_file.name]
            with pytest.raises(NotADirectoryError):
                get_input_dir()
