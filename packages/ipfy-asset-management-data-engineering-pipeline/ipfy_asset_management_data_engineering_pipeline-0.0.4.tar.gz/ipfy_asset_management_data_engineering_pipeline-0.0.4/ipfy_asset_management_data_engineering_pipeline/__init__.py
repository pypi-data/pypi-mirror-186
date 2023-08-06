"""IPFY Asset Management Data Pipeline"""
#from .CreditAgricoleAlsace._data_integration_pipeline import CreditAgricoleBankDataProcessPipeline
from ._bank_data_type_detection import BankDataTypeDetection
from .orchestration_and_process_execution import OrchestrationAndProcessExecutionPipeline

__all__ = [
    #"CreditAgricoleBankDataProcessPipeline",
    "BankDataTypeDetection",
    "OrchestrationAndProcessExecutionPipeline"
]
