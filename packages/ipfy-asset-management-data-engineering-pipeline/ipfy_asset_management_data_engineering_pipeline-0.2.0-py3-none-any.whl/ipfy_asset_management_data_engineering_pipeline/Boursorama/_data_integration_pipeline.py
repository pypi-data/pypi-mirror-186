"""Data process on Credit Agricole bank data"""

import pandas as pd
import numpy as np


class BoursoramaBankDataProcessPipeline:
    """class that process boursorama bank data"""

    # init method or constructor
    def __init__(self, bank_records_dataframe: pd.DataFrame):
        self.bank_records_dataframe = bank_records_dataframe

    def drop_specific_rows(self) -> pd.DataFrame:

        # Remove if operation date is '
        self.bank_records_dataframe = self.bank_records_dataframe.drop(
            self.bank_records_dataframe[
                self.bank_records_dataframe.operation_date == "'"
            ].index
        )
        # Drop row that are all na
        self.bank_records_dataframe = self.bank_records_dataframe.dropna(how="all")

        return self.bank_records_dataframe

    def clean_values_bank_records_df(self) -> pd.DataFrame:
        """clean, process and format data values in the dataframe"""

        for col in self.bank_records_dataframe.columns:
            self.bank_records_dataframe[col] = self.bank_records_dataframe[
                col
            ].str.replace("'", "", regex=False)
            if col in ["debit", "credit"]:
                self.bank_records_dataframe[col] = self.bank_records_dataframe[
                    col
                ].str.replace(".", "", regex=False)
                self.bank_records_dataframe[col] = self.bank_records_dataframe[
                    col
                ].str.replace(",", ".", regex=False)
                self.bank_records_dataframe[col] = np.where(
                    self.bank_records_dataframe[col] == "",
                    0,
                    self.bank_records_dataframe[col],
                )
                self.bank_records_dataframe[col] = (
                    self.bank_records_dataframe[col]
                    .str.replace(" ", "", regex=False)
                    .astype(float)
                )
                self.bank_records_dataframe[col] = self.bank_records_dataframe[
                    col
                ].fillna(0)
            if col in ["operation_description", "operation_date"]:
                self.bank_records_dataframe[col] = self.bank_records_dataframe[
                    col
                ].str.strip()

        return self.bank_records_dataframe

    def operation_date_to_datetime(self) -> pd.DataFrame:
        """operation_date as datetime format"""

        # Date processing
        self.bank_records_dataframe["operation_date"] = pd.to_datetime(
            self.bank_records_dataframe["operation_date"], format="%d/%m/%Y"
        )

        return self.bank_records_dataframe

    def get_correct_columns_order(self) -> pd.DataFrame:
        """Re-order the dataframe"""
        self.bank_records_dataframe = self.bank_records_dataframe[
            ["operation_date", "operation_description", "debit", "credit"]
        ]

        return self.bank_records_dataframe
