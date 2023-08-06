"""Boursorama bank process"""

from .data_pipeline_execution import data_structure_unification
from ._data_integration_pipeline import BoursoramaBankDataProcessPipeline

__all__ = [
    "data_structure_unification",
    "BoursoramaBankDataProcessPipeline",
]
