# pylint: disable=protected-access
from diffant.report.raw import RawReportGenerator
from diffant.differ.types import DiffSummary, KeySummary, ValueSummary


def test_report_happy_path():
    report = RawReportGenerator()
    diff_summary = DiffSummary(
        keys=[
            KeySummary(
                key_path=["a"],
                values=[
                    ValueSummary(
                        value=1,
                        filenames={"test.json", "test2.json"},
                    )
                ],
            )
        ],
        filenames={"test.json", "test2.json"},
    )
    report.generate_report(diff_summary=diff_summary)
