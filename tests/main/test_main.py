from pathlib import Path

import pytest

from diffant import exceptions  # pylint: disable = unused-import
from diffant.main import main


def test_main(mocker):
    current_dir = Path(__file__).resolve().parent
    config_dir_relative = current_dir / "../data/json/simple/"
    absolute_path = config_dir_relative.resolve()

    mocker.patch("diffant.main.get_input_dir", return_value=absolute_path)
    mocker.patch("diffant.main.get_config_files_type", return_value="json")
    assert main()


def test_main_catches(mocker):
    current_dir = Path(__file__).resolve().parent
    config_dir_relative = current_dir / "../data/json/simple/"
    absolute_path = config_dir_relative.resolve()

    mocker.patch("diffant.main.get_input_dir", return_value=absolute_path)
    mocker.patch(
        "diffant.main.get_config_files_type",
        side_effect=exceptions.FatalButExpectedError("Invalid directory"),
    )
    with pytest.raises(SystemExit) as exc:
        main()
        assert "Invalid directory" in str(exc)
