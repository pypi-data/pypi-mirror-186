from typing import List
import pandas as pd
import numpy as np

class CreditAgricoleBankDataProcessPipeline:
    """
    """
    # # init method or constructor
    # def __init__(self, bank_records_dataframe):
    #     self.bank_records_data = bank_records_data

    def clean_values_bank_records_df(bank_records_dataframe) -> pd.DataFrame:

        for col in bank_records_dataframe.columns:
            bank_records_dataframe[col] = bank_records_dataframe[col].str.replace("'", "")
            if col in ['debit', 'credit']:
                bank_records_dataframe[col] = bank_records_dataframe[col].str.replace(",", ".")
                bank_records_dataframe[col] = np.where(
                    bank_records_dataframe[col]=="",
                    0,
                    bank_records_dataframe[col])
                bank_records_dataframe[col] = bank_records_dataframe[col].str.replace(" ", "").astype(float)
                bank_records_dataframe[col] = bank_records_dataframe[col].fillna(0)
            if col in ['operation_description']:
                bank_records_dataframe[col] = bank_records_dataframe[col].str.strip()

        return bank_records_dataframe

    def drop_row_w_no_values(bank_records_dataframe):
        # Drp row where Debit and Credit are Null
        bank_records_dataframe = bank_records_dataframe.drop(
            bank_records_dataframe[
                    (bank_records_dataframe.debit == 0) &
                    (bank_records_dataframe.credit == 0)
                ].index
            )
        return bank_records_dataframe


    def get_unique_date_of_operation(bank_records_dataframe) -> pd.DataFrame:
        # Date process and unification
        bank_records_dataframe['operation_date'] = np.where(
            bank_records_dataframe['operation_date'].isna(), 
            bank_records_dataframe['value_date'],
            bank_records_dataframe['operation_date']
        ) 

        bank_records_dataframe['value_date'] = np.where(
            bank_records_dataframe['value_date'].isna(), 
            bank_records_dataframe['operation_date'],
            bank_records_dataframe['value_date']
        ) 

        bank_records_dataframe['date_operation'] = bank_records_dataframe['value_date']

        bank_records_dataframe['date_operation'] = np.where(
            bank_records_dataframe['date_operation'].isna(),
            bank_records_dataframe['operation_date'],
            bank_records_dataframe['date_operation'])

        bank_records_dataframe = bank_records_dataframe.drop(['operation_date', 'value_date'], axis=1, errors='ignore')
        bank_records_dataframe = bank_records_dataframe.rename({'date_operation': 'operation_date'}, axis=1)

        return bank_records_dataframe