"""
Class that detect the type of bank from the unifed dta file initally created from zip
"""

import dataclasses


@dataclasses.dataclass
class BankDataTypeDetection:
    """
    Data Process to detect the bank type
    """

    def get_bank_file_type_from_strucutre(self, bank_records_data_columns: list) -> str:
        """
        From the dataframe strucutre we defined the function we want to run to unified the data
        """

        # List strucutre from different banks
        columns_credit_agricole_type_1 = [
            "'Date ope. ",
            "'Date valeur ",
            "'Libellé des opérations ",
            "'Débit ",
            "'Crédit ",
            "'",
            "Unnamed: 6",
            "'Date opé. ",
        ]
        columns_credit_agricole_type_2 = [
            "'Date ope. ",
            "'Date valeur ",
            "'Libellé des opérations ",
            "'Débit ",
            "'Crédit ",
            "'",
            "Unnamed: 6",
        ]

        columns_boursorama_banque = [
            "'Date ",
            "'N° de RIB ",
            "'",
            "'.1",
            "'.2",
            "'Devise ",
            "'Période ",
            "'Montant DA* ",
            "'TAEG* ",
            "'Page ",
            "Unnamed: 10",
            "'Date opération ",
            "'Libellé ",
            "'Valeur ",
            "'Débit ",
            "'Crédit ",
            "Unnamed: 5",
        ]

        columns_canext_banque = [
            "'DATE ",
            "'OPERATION DETAIL ",
            "'DEBIT ",
            "'CREDIT ",
            "'VALEUR ",
            "'SOLDE CHF ",
            "Unnamed: 6",
        ]

        if (bank_records_data_columns == columns_credit_agricole_type_1) | (
            bank_records_data_columns == columns_credit_agricole_type_2
        ):
            return "CreditAgricoleAlsace"

        if bank_records_data_columns == columns_boursorama_banque:
            return "BoursoramaBanque"

        if bank_records_data_columns == columns_canext_banque:
            return "CreditAgricoleNextBank"

        if (
            (bank_records_data_columns != columns_credit_agricole_type_1)
            & (bank_records_data_columns != columns_credit_agricole_type_2)
            & (bank_records_data_columns != columns_boursorama_banque)
            & (bank_records_data_columns != columns_canext_banque)
        ):
            return "DontKnowYet"

        return None
