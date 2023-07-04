"""Raw report generation."""
from diffant.differ.types import DiffSummary
from diffant.report.abc import ReportGeneratorABC


class RawReportGenerator(ReportGeneratorABC):
    """Report generator that outputs a raw string."""

    def generate_report(self, diff_summary: DiffSummary) -> str:
        """
        Generate a human-readable string representation of
        the difference between key/values found in config files.

        This method formats a dictionary of key-value pairs and corresponding config
        filenames into a readable string. The  keys follow the pattern
        'key:sub_key:sub_key:', extracted from the original confg file. The inner
        dictionary contains  'values' as keys pointing to a list of filenames where
        the outer key (e.g., 'fruit') can be found.

            Example:
                fruit:  apple
                        tests/sample_input.d/file01.json
                        tests/sample_input.d/file03.json

                        cherry
                        tests/sample_input.d/file02.json

        """
        indent = " " * 4
        report = ""

        for key_summary in diff_summary.keys:
            key_path_str = ":".join(key_summary.key_path)
            report += f"{key_path_str}\n"
            filenames = set()
            for value_summary in key_summary.values:
                report += f"{indent}{value_summary.value}\n"
                for filename in value_summary.filenames:
                    report += f"{indent}{indent}{filename}\n"
                    filenames.add(filename)
            missing_files = set(diff_summary.filenames) - filenames
            if missing_files:
                report += f"{indent}/*MISSING*/\n"
                for filename in missing_files:
                    report += f"{indent}{indent}{filename}\n"

        print(report)
        return report
