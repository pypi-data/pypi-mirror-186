from typing import List
import pandas as pd

class DataProcessAndUnificationPipeline:
    """
    """

    # init method or constructor
    def __init__(self, bank_records_data):
        self.bank_records_data = bank_records_data

    def get_bank_file_type_from_strucutre(self) -> str:
        """
        From the dataframe strucutre we defined the function we want to run to unified the data
        """

        bank_dataframe = self.bank_records_data
        columns_credit_agricole = ["'Date ope. ", "'Date valeur ", "'Libellé des opérations ", "'Débit ", "'Crédit ", "'", "Unnamed: 6", "'Date opé. "]

        if list(bank_dataframe.columns) == columns_credit_agricole:
            return 'CreditAgricoleAlsace'
        else:
            return 'DontKnowYet'


    def credit_agricole_alsace_unification(self) -> pd.DataFrame:
        """
        From the zipped strucutre we perform transformation step to undify this data
        Unification will allow us to combined all the different baks records type together
        """

        print('OKKKKK')
        
        return 1

    def orchestration_and_process_execution(self):

        bank_file_type = self.get_bank_file_type_from_strucutre()
        
        if bank_file_type == 'CreditAgricoleAlsace':
            self.credit_agricole_alsace_unification()



