"""Orchestration module."""

import dataclasses
import pandas as pd

from ipfy_asset_management_data_engineering_pipeline import (
    BankDataTypeDetection,
    creditagricolealsace,
    creditagricolenextbank,
    boursorama,
)


@dataclasses.dataclass
class OrchestrationAndProcessExecutionPipeline:
    """
    Class doing the Orchestration of the data bank process
    """

    # init method or constructor
    def __init__(self, bank_records_data):
        self.bank_records_data = bank_records_data

    def orchestration_and_process_execution(self) -> pd.DataFrame:
        """
        Orchestration and execution of all the steps
        """

        # Step 1 is to get the bank file type to kn ow witch unification process to execute
        bank_file_type: str = BankDataTypeDetection.get_bank_file_type_from_strucutre(
            self, list(self.bank_records_data.columns)
        )

        # Step 2: According bank_file_type execute the corresponding uniformisation process
        if bank_file_type == "CreditAgricoleAlsace":
            unifed_bank_records: pd.DataFrame = (
                creditagricolealsace.data_structure_unification(self.bank_records_data)
            )

        if bank_file_type == "CreditAgricoleNextBank":
            unifed_bank_records: pd.DataFrame = (
                creditagricolenextbank.data_structure_unification(
                    self.bank_records_data
                )
            )

        if bank_file_type == "BoursoramaBanque":
            unifed_bank_records: pd.DataFrame = boursorama.data_structure_unification(
                self.bank_records_data
            )

        return unifed_bank_records
