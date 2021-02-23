from typing import Optional
from dataclasses import dataclass
from .Address import Address
from .TaxNumber import TaxNumber


@dataclass
class FiscalRepresentative:
    """Fiscal representative data

    :param fiscal_representative_tax_number: Tax number of the fiscal representative
    :param fiscal_representative_name: Name of the fiscal representative
    :param fiscal_representative_address: Address of the fiscal representative
    :param fiscal_representative_bank_account_number: Bank account number opened by the fiscal representative for the issuer of the invoice (supplier)
    """

    fiscal_representative_tax_number: TaxNumber
    fiscal_representative_name: str
    fiscal_representative_address: Address
    fiscal_representative_bank_account_number: Optional[str]
