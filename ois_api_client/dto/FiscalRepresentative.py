from typing import Union

from .Address import Address
from .TaxNumber import TaxNumber


class FiscalRepresentative:
    """Fiscal representative data

    :param fiscal_representative_tax_number: Tax number of the fiscal representative
    :param fiscal_representative_name: Name of the fiscal representative
    :param fiscal_representative_address: Address of the fiscal representative
    :param fiscal_representative_bank_account_number: Bank account number opened by the fiscal representative for the issuer of the invoice (supplier)
    """

    def __init__(self,
                 fiscal_representative_tax_number: TaxNumber,
                 fiscal_representative_name: str,
                 fiscal_representative_address: Address,
                 fiscal_representative_bank_account_number: Union[str, None] = None):
        self.fiscal_representative_tax_number = fiscal_representative_tax_number
        self.fiscal_representative_name = fiscal_representative_name
        self.fiscal_representative_address = fiscal_representative_address
        self.fiscal_representative_bank_account_number = fiscal_representative_bank_account_number
