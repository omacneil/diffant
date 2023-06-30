from pathlib import Path

import pytest

from diffant import exceptions
from diffant.main import get_config_files_type


@pytest.fixture
def temp_dir(tmp_path):
    # Create a temporary directory for testing
    return str(tmp_path)


def test_get_config_files_type_single_extension(temp_dir):
    # Create files with a single extension in the temporary directory
    Path(temp_dir, "file1.json").touch()
    Path(temp_dir, "file2.json").touch()
    Path(temp_dir, "file3.json").touch()

    assert get_config_files_type(temp_dir) == "json"


def test_get_config_files_type_multiple_extensions(temp_dir):
    # Create files with multiple extensions in the temporary directory
    Path(temp_dir, "file1.json").touch()
    Path(temp_dir, "file2.xml").touch()
    Path(temp_dir, "file3.ini").touch()

    with pytest.raises(exceptions.InputDirContentsError) as exc_info:
        get_config_files_type(temp_dir)

    assert "Expected 1 file extension" in str(exc_info.value)


def test_get_config_files_type_subdirectories(temp_dir):
    # Create a subdirectory in the temporary directory
    Path(temp_dir, "subdir").mkdir()

    with pytest.raises(exceptions.InputDirContentsError) as exc_info:
        get_config_files_type(temp_dir)

    assert "Sub-directories not allowed" in str(exc_info.value)


def test_get_config_files_type_no_extension(temp_dir):
    # Create a file without extension in the temporary directory
    Path(temp_dir, "file").touch()

    with pytest.raises(exceptions.InputDirContentsError) as exc_info:
        get_config_files_type(temp_dir)

    assert "Files without extensions not allowed" in str(exc_info.value)
