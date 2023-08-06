"""Data process on Credit Agricole bank data"""

import pandas as pd
import numpy as np

class CreditAgricoleBankDataProcessPipeline:
    """class that process credit agricole bank data"""

    # init method or constructor
    def __init__(self, bank_records_dataframe: pd.DataFrame):
        self.bank_records_dataframe = bank_records_dataframe

    def clean_values_bank_records_df(self) -> pd.DataFrame:
        """clean, process and format data values in the dataframe"""

        for col in self.bank_records_dataframe.columns:
            self.bank_records_dataframe[col] = self.bank_records_dataframe[
                col
            ].str.replace("'", "")
            if col in ["debit", "credit"]:
                self.bank_records_dataframe[col] = self.bank_records_dataframe[
                    col
                ].str.replace(",", ".")
                self.bank_records_dataframe[col] = np.where(
                    self.bank_records_dataframe[col] == "",
                    0,
                    self.bank_records_dataframe[col],
                )
                self.bank_records_dataframe[col] = (
                    self.bank_records_dataframe[col].str.replace(" ", "").astype(float)
                )
                self.bank_records_dataframe[col] = self.bank_records_dataframe[
                    col
                ].fillna(0)
            if col in ["operation_description"]:
                self.bank_records_dataframe[col] = self.bank_records_dataframe[
                    col
                ].str.strip()

        return self.bank_records_dataframe

    def drop_row_w_no_values(self) -> pd.DataFrame:
        """remove data without debit and credit"""
        # Drp row where Debit and Credit are Null
        self.bank_records_dataframe = self.bank_records_dataframe.drop(
            self.bank_records_dataframe[
                (self.bank_records_dataframe.debit == 0)
                & (self.bank_records_dataframe.credit == 0)
            ].index
        )
        return self.bank_records_dataframe

    def get_unique_date_of_operation(self) -> pd.DataFrame:
        """get unique date for each operation"""
        # Date process and unification
        self.bank_records_dataframe["operation_date"] = np.where(
            self.bank_records_dataframe["operation_date"].isna(),
            self.bank_records_dataframe["value_date"],
            self.bank_records_dataframe["operation_date"],
        )

        self.bank_records_dataframe["value_date"] = np.where(
            self.bank_records_dataframe["value_date"].isna(),
            self.bank_records_dataframe["operation_date"],
            self.bank_records_dataframe["value_date"],
        )

        self.bank_records_dataframe["date_operation"] = self.bank_records_dataframe[
            "value_date"
        ]

        self.bank_records_dataframe["date_operation"] = np.where(
            self.bank_records_dataframe["date_operation"].isna(),
            self.bank_records_dataframe["operation_date"],
            self.bank_records_dataframe["date_operation"],
        )

        self.bank_records_dataframe = self.bank_records_dataframe.drop(
            ["operation_date", "value_date"], axis=1, errors="ignore"
        )
        self.bank_records_dataframe = self.bank_records_dataframe.rename(
            {"date_operation": "operation_date"}, axis=1
        )

        return self.bank_records_dataframe

    def get_correct_columns_order(self) -> pd.DataFrame:
        """Re-order the dataframe"""
        self.bank_records_dataframe = self.bank_records_dataframe[
            ["operation_date", "operation_description", "debit", "credit"]
        ]

        return self.bank_records_dataframe
