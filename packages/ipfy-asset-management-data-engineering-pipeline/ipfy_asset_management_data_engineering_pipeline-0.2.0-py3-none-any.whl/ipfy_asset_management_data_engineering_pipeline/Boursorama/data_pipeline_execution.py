"""Data Pipeline for Credit Agricole data type"""

import pandas as pd

from ipfy_asset_management_data_engineering_pipeline import boursorama


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
        [
            "Date",
            "N°deRIB",
            "",
            "1",
            "2",
            "Devise",
            "Période",
            "MontantDA*",
            "TAEG*",
            "Page",
            "Unnamed:10",
            "Unnamed:5",
        ],
        axis=1,
        errors="ignore",
    )

    # Rename columns
    bank_records_dataframe.columns = [
        "operation_date",
        "operation_description",
        "value_date",
        "debit",
        "credit",
    ]

    # Class initalisation
    credit_agricole_bank_data_process = boursorama.BoursoramaBankDataProcessPipeline(
        bank_records_dataframe=bank_records_dataframe
    )

    # Drop ropws where debit and credit don't have values (credit and debit equal to 0)
    bank_records_dataframe = credit_agricole_bank_data_process.drop_specific_rows()

    # Clean values from Bank dataframe records (remove ' character, strp on operation_description)
    bank_records_dataframe = (
        credit_agricole_bank_data_process.clean_values_bank_records_df()
    )

    # Date process and unification
    bank_records_dataframe = (
        credit_agricole_bank_data_process.operation_date_to_datetime()
    )

    # Re-order the columns
    bank_records_dataframe = (
        credit_agricole_bank_data_process.get_correct_columns_order()
    )

    # Reset the index as a final step
    bank_records_dataframe = bank_records_dataframe.reset_index(drop=True)

    return bank_records_dataframe
