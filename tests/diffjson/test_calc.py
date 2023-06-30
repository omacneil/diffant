# pylint: disable=protected-access

import os
from pathlib import Path
from unittest.mock import MagicMock

import pytest

from diffant import exceptions
from diffant.diffjson import DiffJson


def test_calc_happy_path():
    diff = DiffJson()  # use an instance of the concrete class

    current_dir = Path(__file__).resolve().parent
    config_dir_relative = current_dir / "../data/json/simple/"
    config_dir = str(config_dir_relative.resolve())
    diff.calc(config_dir=config_dir, files_type="json")


def test_calc_handles_FileNotFoundError():
    """Test when _get_config_files throws a FileNotFoundError"""
    diff = DiffJson()  # use an) instance of the concrete class
    current_dir = Path(__file__).resolve().parent
    config_dir_relative = current_dir / "../data/json/simple/"
    config_dir = str(config_dir_relative.resolve())
    diff._get_config_files = MagicMock(side_effect=FileNotFoundError("test error"))

    with pytest.raises(SystemExit) as exc_info:
        diff.calc(config_dir=config_dir, files_type="json")
        assert exc_info.value.code == os.EX_DATAERR


def test_calc_handles_FatalButExpectedError():
    """Test when _get_config_files throws a FileNotFoundError"""
    diff = DiffJson()  # use an instance of the concrete class
    current_dir = Path(__file__).resolve().parent
    config_dir_relative = current_dir / "../data/json/simple/"
    config_dir = str(config_dir_relative.resolve())
    diff._parse_config_files = MagicMock(
        side_effect=exceptions.FatalButExpectedError("test error")
    )

    with pytest.raises(SystemExit) as exc_info:
        diff.calc(config_dir, files_type="json")
        assert exc_info.value.code == os.EX_DATAERR
