"""Interface for report generators."""
from abc import ABC, abstractmethod
from typing import Any

from diffant.differ.types import DiffSummary


class ReportGeneratorABC(ABC):
    """Abstract report generator."""

    @abstractmethod
    def generate_report(self, data: DiffSummary) -> Any:
        """Generate a report from the diff summary."""
        pass
