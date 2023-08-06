"""IPFY Asset Management Data Pipeline"""

from ._bank_data_type_detection import BankDataTypeDetection
from .orchestration_and_process_execution import (
    OrchestrationAndProcessExecutionPipeline,
)

__all__ = [
    "BankDataTypeDetection",
    "OrchestrationAndProcessExecutionPipeline",
]
