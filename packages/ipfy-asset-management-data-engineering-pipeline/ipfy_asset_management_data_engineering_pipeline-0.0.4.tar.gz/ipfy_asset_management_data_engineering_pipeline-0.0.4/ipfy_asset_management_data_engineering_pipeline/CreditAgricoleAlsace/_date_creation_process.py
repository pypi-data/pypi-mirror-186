from typing import List
import pandas as pd
import numpy as np
import sys

class CreditAgricoleDatetimeValueProcess:
    """
    """

    def get_year_bank_records(bank_records_dataframe):

        # If we don't have date from Credit Agricole files that means this is a summary at a specifc date of time
        bank_records_dataframe_tot_operations = bank_records_dataframe[
            (bank_records_dataframe['operation_date']=='') &
            (bank_records_dataframe['operation_description']!='Total des opérations')
            ].copy()

        # STEP 2
        bank_records_dataframe_tot_operations['operation_date'] = pd.to_datetime(
            bank_records_dataframe_tot_operations['operation_description'].str[-10:], format="%d.%m.%Y"
            )

        # Get year of bank records
        year_bank_records = bank_records_dataframe_tot_operations['operation_date'][
            bank_records_dataframe_tot_operations['operation_description'].str.contains('Ancien solde')
            ].dt.year

        return year_bank_records

    def remove_row_without_date(bank_records_dataframe):

        # Drp row where Debit and Credit are Null
        bank_records_dataframe = bank_records_dataframe.drop(
            bank_records_dataframe[
                    bank_records_dataframe['operation_date'] == ''
                ].index
            )
        return bank_records_dataframe

    def get_operation_date_as_datetype(bank_records_dataframe, year_bank_records):

        # Using year we assign year to date operation
        bank_records_dataframe['operation_date'] = bank_records_dataframe['operation_date'] + '.' + str(year_bank_records[0])
        bank_records_dataframe['operation_date'] = bank_records_dataframe['operation_date'].str.replace(' ','')
        bank_records_dataframe['operation_date'] = pd.to_datetime(bank_records_dataframe['operation_date'], format="%d.%m.%Y")

        return bank_records_dataframe


    def year_modification_december_bank_file(bank_records_dataframe):
        """
        For bank records in December it might be possible to have two different years
        From the previous processstep all the records will have by defauklt the year_bank_records as year.
        This process is a temporary solution to solve this issue
        """

        month_distribution = pd.DataFrame(bank_records_dataframe.operation_date.dt.month.value_counts()).reset_index()
        month_distribution.columns = ['month', 'count']
        month_distribution = month_distribution.sort_values(by='count', ascending=False)
        most_present_months = month_distribution['month'].head(1).values[0]

        if most_present_months == 12:
            bank_records_dataframe['operation_date'] = np.where(
                bank_records_dataframe['operation_date'].dt.month==1,
                bank_records_dataframe['operation_date'] + pd.offsets.DateOffset(years=1),
                bank_records_dataframe['operation_date']
            )

        return bank_records_dataframe
