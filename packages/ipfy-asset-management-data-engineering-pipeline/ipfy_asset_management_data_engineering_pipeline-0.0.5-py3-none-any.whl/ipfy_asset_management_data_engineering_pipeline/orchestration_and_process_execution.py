from typing import List
import pandas as pd

from ipfy_asset_management_data_engineering_pipeline import BankDataTypeDetection
from ipfy_asset_management_data_engineering_pipeline.CreditAgricoleAlsace.data_pipeline_execution import data_structure_unification 

class OrchestrationAndProcessExecutionPipeline:
    """
    Orchestration and execution of all the steps
    """

    # init method or constructor
    def __init__(self, bank_records_data):
        self.bank_records_data = bank_records_data

    def orchestration_and_process_execution(self) -> pd.DataFrame:

        # Step 1 is to get the bank file type to kn ow witch unification process to execute
        bank_file_type: str = BankDataTypeDetection.get_bank_file_type_from_strucutre(self, self.bank_records_data.columns)

        # Step 2: According bank_file_type execute the corresponding uniformisation process
        if bank_file_type == 'CreditAgricoleAlsace':
            unifed_bank_records: pd.DataFrame = data_structure_unification(self.bank_records_data)

        if bank_file_type == 'BoursoramaBanque':
            print('Need to create the class')

        return unifed_bank_records
