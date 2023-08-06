"""Data Pipeline for Credit Agricole data type"""

import pandas as pd

from ipfy_asset_management_data_engineering_pipeline import creditagricolealsace


def data_structure_unification(bank_records_dataframe) -> pd.DataFrame:
    """
    From the zipped strucutre we perform transformation step to unify the data
    Unification will allow us to combined all the different banks records type together
    """

    # Reset the index because there are different from the previous file unification step
    bank_records_dataframe = bank_records_dataframe.reset_index(drop=True)

    # String fromating on the columns
    bank_records_dataframe.columns = bank_records_dataframe.columns.str.replace(
        "'", "", regex=False
    )
    bank_records_dataframe.columns = bank_records_dataframe.columns.str.replace(
        ".", "", regex=False
    )
    bank_records_dataframe.columns = bank_records_dataframe.columns.str.replace(
        " ", "", regex=False
    )

    # Drop the non needed columns
    bank_records_dataframe = bank_records_dataframe.drop(
        ["Unnamed:6", "Dateopé", ""], axis=1, errors="ignore"
    )

    # Rename columns
    bank_records_dataframe.columns = [
        "operation_date",
        "value_date",
        "operation_description",
        "debit",
        "credit",
    ]

    # Class initalisation
    credit_agricole_bank_data_process = (
        creditagricolealsace.CreditAgricoleBankDataProcessPipeline(
            bank_records_dataframe=bank_records_dataframe
        )
    )

    # Clean values from Bank dataframe records (remove ' character, strp on operation_description)
    bank_records_dataframe = (
        credit_agricole_bank_data_process.clean_values_bank_records_df()
    )

    # Drop ropws where debit and credit don't have values (credit and debit equal to 0)
    bank_records_dataframe = credit_agricole_bank_data_process.drop_row_w_no_values()

    # Date process and unification
    bank_records_dataframe = (
        credit_agricole_bank_data_process.get_unique_date_of_operation()
    )

    # Class initialisation with the dataframe

    credit_agricole_date_process = (
        creditagricolealsace.CreditAgricoleDatetimeValueProcess(
            bank_records_dataframe=bank_records_dataframe
        )
    )

    # Operation date as datetype
    year_bank_records = credit_agricole_date_process.get_year_bank_records()
    bank_records_dataframe = credit_agricole_date_process.remove_row_without_date()
    bank_records_dataframe = (
        credit_agricole_date_process.get_operation_date_as_datetype(year_bank_records)
    )
    bank_records_dataframe = (
        credit_agricole_date_process.year_modification_december_bank_file()
    )

    # Re-order the columns
    bank_records_dataframe = (
        credit_agricole_bank_data_process.get_correct_columns_order()
    )

    # Reset the index as a final step
    bank_records_dataframe = bank_records_dataframe.reset_index(drop=True)

    return bank_records_dataframe
