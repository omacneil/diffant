""" test _set_report() method"""
# pylint: disable=protected-access

from diffant.diffjson import DiffJson


def test__set_report():
    """given a data structure do we get back the string
    we expect
    """
    input_data = {
        "key1": {
            "values": {
                "value1": ["filename1", "filename2"],
                "value2": ["filename3", "filename4"],
            }
        },
        "key2": {
            "values": {
                "value3": ["filename5", "filename6"],
                "value4": ["filename7", "filename8"],
            }
        },
    }
    expected_result = (
        """key1  value1
        filename1
        filename2

      value2
        filename3
        filename4

key2  value3
        filename5
        filename6

      value4
        filename7
        filename8
"""
        + "\n"
    )
    # Execution
    differ = DiffJson()
    differ._flat_recs = input_data
    differ._set_report()

    assert differ._report == expected_result
