"""Command line interface for diffant."""
from enum import Enum
from typing import TYPE_CHECKING, Iterable, List, Protocol, Set

if TYPE_CHECKING:
    from diffant.differ.types import ConfigData, DiffSummary

import typer

app = typer.Typer()


class ReportTypeEnum(str, Enum):
    """Report type."""
    raw = "raw"


class PathLike(Protocol):
    """Protocol for a path-like object."""

    @property
    def name(self) -> str:
        """Get the name of the file."""
        ...

    @property
    def suffix(self) -> str:
        """Get the suffix of the file."""
        ...

    def glob(self, pattern) -> Iterable["PathLike"]:
        """Get the file paths matching the given pattern."""
        ...



@app.command()
def main(
    input_dir: str = typer.Argument(
        ...,
        help="Directory with configuration files to diff",
    ),
    input_patterns: List[str] = typer.Option(
        None,
        "--input-pattern",
        "-p",
        help="Glob pattern to match files in input dir",
    ),
    is_cloud_path: bool = typer.Option(
        False,
        "--is-cloud-path",
        "-c",
        help=("If the input dir is a cloud path, " "e.g. gs://my-bucket/my-dir"),
    ),
    report_type: ReportTypeEnum = typer.Option(
        ReportTypeEnum.raw, "--report-type", "-r", help="Type of report to generate."
    ),
) -> None:
    """Diff configuration files in a directory"""
    file_paths = get_file_paths(
        input_dir=input_dir,
        input_patterns=input_patterns or ["*"],
        is_cloud_path=is_cloud_path,
    )
    config_data = get_config_data(file_paths, is_cloud_path)
    diff_summary = get_diff_summary(config_data)
    generate_report(diff_summary, report_type)


def get_file_paths(
    input_dir: str, input_patterns: List[str], is_cloud_path: bool
) -> Set[PathLike]:
    """Get the file paths at a given input_dir."""
    input_dir_path: PathLike

    if is_cloud_path:
        from cloudpathlib import CloudPath

        input_dir_path = CloudPath(input_dir) # type: ignore [abstract]
    else:
        from pathlib import Path

        input_dir_path = Path(input_dir)

    file_paths: Set[PathLike] = set()
    for input_pattern in input_patterns:
        for path in input_dir_path.glob(input_pattern):
            file_paths.add(path)

    return file_paths


def get_config_data(file_paths: Set[PathLike], is_cloud_path: bool) -> List["ConfigData"]:
    """Get the file contents at a given file path."""
    from diffant.deserializer import deserialize
    from diffant.differ.types import ConfigData
    from diffant.reader import read_file

    return [
        ConfigData(
            filename=file_path.name,
            data=deserialize(
                file_contents=read_file(str(file_path), is_cloud_path), suffix=file_path.suffix
            ),
        )
        for file_path in file_paths
    ]


def get_diff_summary(config_data: List["ConfigData"]) -> "DiffSummary":
    """Get the diff summary between the given config data."""
    from diffant.differ.differ import Differ

    return Differ().calc(*config_data)


def generate_report(diff_summary: "DiffSummary", report_type: ReportTypeEnum) -> None:
    """Generate a report from the diff summary."""
    from diffant.report.generate import generate_report

    generate_report(diff_summary, report_type)


if __name__ == "__main__":
    app()
