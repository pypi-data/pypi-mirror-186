"""Data process on Credit Agricole bank data"""

import pandas as pd
import numpy as np
import pkg_resources


class CreditAgricoleNextBankDataProcessPipeline:
    """class that process credit agricole bank data"""

    # init method or constructor
    def __init__(self, bank_records_dataframe: pd.DataFrame):
        self.bank_records_dataframe = bank_records_dataframe

    def clean_values_bank_records_df(self) -> pd.DataFrame:
        """clean, process and format data values in the dataframe"""

        for col in self.bank_records_dataframe.columns:
            self.bank_records_dataframe[col] = self.bank_records_dataframe[
                col
            ].str.replace("'", "", regex=False)
            if col in ["debit", "credit"]:
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

    def drop_specific_rows(self) -> pd.DataFrame:
        """remove data without debit and credit"""
        # Drp row where Debit and Credit are Null
        self.bank_records_dataframe = self.bank_records_dataframe.drop(
            self.bank_records_dataframe[
                (self.bank_records_dataframe.debit == 0)
                & (self.bank_records_dataframe.credit == 0)
            ].index
        )

        # Remove if operation date is '
        self.bank_records_dataframe = self.bank_records_dataframe[
            self.bank_records_dataframe["operation_date"] != ""
        ]

        # Remove if operation date is SOLDE
        self.bank_records_dataframe = self.bank_records_dataframe[
            self.bank_records_dataframe["operation_date"] != "SOLDE "
        ]

        # Drop row that are all na
        self.bank_records_dataframe = self.bank_records_dataframe.dropna(how="all")

        return self.bank_records_dataframe

    def operation_date_to_datetime(self) -> pd.DataFrame:
        """operation_date as datetime format"""

        # Date processing
        self.bank_records_dataframe["operation_date"] = pd.to_datetime(
            self.bank_records_dataframe["operation_date"], format="%d.%m.%y"
        )

        return self.bank_records_dataframe

    def get_correct_columns_order(self) -> pd.DataFrame:
        """Re-order the dataframe"""
        self.bank_records_dataframe = self.bank_records_dataframe[
            ["operation_date", "operation_description", "debit", "credit"]
        ]

        return self.bank_records_dataframe

    def chf_to_euro_conversion(self) -> pd.DataFrame:
        """
        convert chf to euros
        data coming from https://www.macrotrends.net/2552/euro-swiss-franc-exchange-rate-historical-chart
        """

        euro_chf_rate_file = pkg_resources.resource_filename(
            "ipfy_asset_management_data_engineering_pipeline",
            "constants/euro-swiss-franc-exchange-rate-historical.csv",
        )

        euro_chf_rate = pd.read_csv(euro_chf_rate_file, sep=",")

        euro_chf_rate["date"] = pd.to_datetime(euro_chf_rate["date"], format="%Y-%m-%d")

        # Left join on date

        self.bank_records_dataframe = pd.merge(
            self.bank_records_dataframe,
            euro_chf_rate,
            left_on="operation_date",
            right_on="date",
            how="left",
        )

        self.bank_records_dataframe["debit"] = round(
            self.bank_records_dataframe["debit"] / self.bank_records_dataframe["rate"],
            2,
        )
        self.bank_records_dataframe["credit"] = round(
            self.bank_records_dataframe["credit"] / self.bank_records_dataframe["rate"],
            2,
        )

        self.bank_records_dataframe = self.bank_records_dataframe.drop(
            ["rate", "date"], axis=1
        )

        return self.bank_records_dataframe
