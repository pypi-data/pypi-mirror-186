"""Data Pipeline for Credit Agricole data type"""

import pandas as pd

from ipfy_asset_management_data_engineering_pipeline import creditagricolenextbank


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
        ["SOLDECHF", "Unnamed:6"], axis=1, errors="ignore"
    )

    # Rename columns
    bank_records_dataframe.columns = [
        "operation_date",
        "operation_description",
        "debit",
        "credit",
        "value_date",
    ]

    # Class initalisation
    credit_agricole_bank_data_process = (
        creditagricolenextbank.CreditAgricoleNextBankDataProcessPipeline(
            bank_records_dataframe=bank_records_dataframe
        )
    )

    # Clean values from Bank dataframe records (remove ' character, strp on operation_description)
    bank_records_dataframe = (
        credit_agricole_bank_data_process.clean_values_bank_records_df()
    )

    # Drop ropws where debit and credit don't have values (credit and debit equal to 0)
    bank_records_dataframe = credit_agricole_bank_data_process.drop_specific_rows()

    # Date process and unification
    bank_records_dataframe = (
        credit_agricole_bank_data_process.operation_date_to_datetime()
    )

    # chf to euros
    bank_records_dataframe = credit_agricole_bank_data_process.chf_to_euro_conversion()

    # Re-order the columns
    bank_records_dataframe = (
        credit_agricole_bank_data_process.get_correct_columns_order()
    )

    # Reset the index as a final step
    bank_records_dataframe = bank_records_dataframe.reset_index(drop=True)

    return bank_records_dataframe
