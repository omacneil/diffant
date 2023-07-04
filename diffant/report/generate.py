from diffant.differ.types import DiffSummary


def generate_report(diff_summary: "DiffSummary", report_type: str) -> None:
    """Generate a report from the diff summary."""
    if report_type == "raw":
        from .raw import RawReportGenerator

        report_generator = RawReportGenerator()
    else:
        raise NotImplementedError(f"Report type {report_type} not implemented.")

    report_generator.generate_report(diff_summary)
