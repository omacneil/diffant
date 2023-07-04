"""Differ types."""
from dataclasses import dataclass
from typing import Any, Dict, List, Set


@dataclass(frozen=True)
class ConfigData:
    """
    Holds the config data for a single config file.
    """

    filename: str
    data: Dict[str, Any]


MISSING = object()


@dataclass
class ValueSummary:
    """
    Holds the value summary.
    """

    value: Any
    filenames: Set[str]


@dataclass
class KeySummary:
    """
    Holds the key summary.
    """

    key_path: List[str]
    values: List[ValueSummary]


@dataclass
class DiffSummary:
    """
    Holds the difference summary.

    key: value, filename, is_missing, diff_count
    """

    keys: List[KeySummary]
    filenames: Set[str]
