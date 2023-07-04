from diffant.differ.differ import Differ
from diffant.differ.types import ConfigData


def test_calc_happy_path():
    differ = Differ() 
    differ.calc(ConfigData(
        filename="test.json",
        data={"a": 1, "b": 2},
    ),
        ConfigData(
            filename="test2.json",
            data={"a": 1, "b": 2},
        ),
    )

