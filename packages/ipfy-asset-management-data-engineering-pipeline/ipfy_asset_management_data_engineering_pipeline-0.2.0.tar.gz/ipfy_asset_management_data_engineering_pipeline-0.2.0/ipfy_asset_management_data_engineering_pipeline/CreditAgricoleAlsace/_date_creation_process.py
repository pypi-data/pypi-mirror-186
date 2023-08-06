"""Date process on CreditAgricole data module."""

import pandas as pd
import numpy as np


class CreditAgricoleDatetimeValueProcess:
    """
    Class that process date from Credit Agricole data file
    """

    def __init__(self, bank_records_dataframe: pd.DataFrame):
        self.bank_records_dataframe = bank_records_dataframe

    def get_year_bank_records(self) -> int:
        """
        function to get the year of the Credit Agricole bank records
        """

        # If we don't have date from Credit Agricole files
        # It means this is a summary at a specifc date of time
        bank_records_dataframe_tot_operations = self.bank_records_dataframe[
            (self.bank_records_dataframe["operation_date"] == "")
            & (
                self.bank_records_dataframe["operation_description"]
                != "Total des opérations"
            )
        ].copy()

        # STEP 2
        bank_records_dataframe_tot_operations["operation_date"] = pd.to_datetime(
            bank_records_dataframe_tot_operations["operation_description"].str[-10:],
            format="%d.%m.%Y",
        )

        # Get year of bank records
        year_bank_records = bank_records_dataframe_tot_operations["operation_date"][
            bank_records_dataframe_tot_operations["operation_description"].str.contains(
                "Ancien solde"
            )
        ].dt.year

        year_bank_records = year_bank_records[0]

        return year_bank_records

    def remove_row_without_date(self) -> pd.DataFrame:
        """
        function that remove operation without date
        """

        # Drp row where Debit and Credit are Null
        self.bank_records_dataframe = self.bank_records_dataframe.drop(
            self.bank_records_dataframe[
                self.bank_records_dataframe["operation_date"] == ""
            ].index
        )
        return self.bank_records_dataframe

    def get_operation_date_as_datetype(self, year_bank_records: int) -> pd.DataFrame:
        """
        function that convert the date to datetype
        """

        # Using year we assign year to date operation
        self.bank_records_dataframe["operation_date"] = (
            self.bank_records_dataframe["operation_date"] + "." + str(year_bank_records)
        )
        self.bank_records_dataframe["operation_date"] = self.bank_records_dataframe[
            "operation_date"
        ].str.replace(" ", "")
        self.bank_records_dataframe["operation_date"] = pd.to_datetime(
            self.bank_records_dataframe["operation_date"], format="%d.%m.%Y"
        )

        return self.bank_records_dataframe

    def year_modification_december_bank_file(self) -> pd.DataFrame:
        """
        For bank records in December it might be possible to have two different years
        From the previous process step all the records has the year_bank_records as year
        This process is a temporary solution to solve this issue
        """

        month_distribution = pd.DataFrame(
            self.bank_records_dataframe.operation_date.dt.month.value_counts()
        ).reset_index()
        month_distribution.columns = ["month", "count"]
        month_distribution = month_distribution.sort_values(by="count", ascending=False)
        most_present_months = month_distribution["month"].head(1).values[0]

        if most_present_months == 12:
            self.bank_records_dataframe["operation_date"] = np.where(
                self.bank_records_dataframe["operation_date"].dt.month == 1,
                self.bank_records_dataframe["operation_date"]
                + pd.offsets.DateOffset(years=1),
                self.bank_records_dataframe["operation_date"],
            )

        return self.bank_records_dataframe
