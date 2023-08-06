from typing import List
import pandas as pd
import numpy as np

from ipfy_asset_management_data_engineering_pipeline.CreditAgricoleAlsace import CreditAgricoleBankDataProcessPipeline
from ipfy_asset_management_data_engineering_pipeline.CreditAgricoleAlsace import CreditAgricoleDatetimeValueProcess

def data_structure_unification(bank_records_dataframe) -> pd.DataFrame:
    """
    From the zipped strucutre we perform transformation step to unify the data
    Unification will allow us to combined all the different banks records type together
    """

    # Reset the index because there are different from the previous file unification step
    bank_records_dataframe = bank_records_dataframe.reset_index(drop=True)

    # String fromating on the columns
    bank_records_dataframe.columns = bank_records_dataframe.columns.str.replace("'", "", regex=False)
    bank_records_dataframe.columns = bank_records_dataframe.columns.str.replace(".", "", regex=False)
    bank_records_dataframe.columns = bank_records_dataframe.columns.str.replace(" ", "", regex=False)

    # Drop the non needed columns
    bank_records_dataframe = bank_records_dataframe.drop(['Unnamed:6', 'Dateopé', ''], axis=1, errors='ignore')

    # Rename columns
    bank_records_dataframe.columns = ['operation_date', 'value_date', 'operation_description',	'debit', 'credit']

    # Clean values from Bank dataframe records (remove ' character, strp on operation_description)
    bank_records_dataframe = CreditAgricoleBankDataProcessPipeline.clean_values_bank_records_df(bank_records_dataframe)

    # Drop ropws where debit and credit don't have values (credit and debit equal to 0)
    bank_records_dataframe = CreditAgricoleBankDataProcessPipeline.drop_row_w_no_values(bank_records_dataframe)

    # Date process and unification
    bank_records_dataframe = CreditAgricoleBankDataProcessPipeline.get_unique_date_of_operation(bank_records_dataframe)
    
    # Operation date as datetype
    year_bank_records = CreditAgricoleDatetimeValueProcess.get_year_bank_records(bank_records_dataframe)
    bank_records_dataframe = CreditAgricoleDatetimeValueProcess.remove_row_without_date(bank_records_dataframe)
    bank_records_dataframe = CreditAgricoleDatetimeValueProcess.get_operation_date_as_datetype(bank_records_dataframe, year_bank_records)
    bank_records_dataframe = CreditAgricoleDatetimeValueProcess.year_modification_december_bank_file(bank_records_dataframe)

    # Re-order the columns
    bank_records_dataframe = CreditAgricoleBankDataProcessPipeline.get_correct_columns_order(bank_records_dataframe)

    # Reset the index as a final step
    bank_records_dataframe = bank_records_dataframe.reset_index(drop=True)

    return bank_records_dataframe