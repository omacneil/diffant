"""
code coverage for report() getter
"""
# pylint: disable=protected-access
from diffant.diffjson import DiffJson


def test_report_property():
    """
    code coverage for report() getter
    """
    diff_json = DiffJson()

    # assign a value to _report_str
    # pylint: disable=protected-access
    diff_json._report = "Test report"

    # Execution & Assertion
    # Call the report property and assert it returns the expected value
    assert diff_json.report == "Test report"
