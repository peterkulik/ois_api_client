from typing import Optional
from dataclasses import dataclass
from .Address import Address
from .TaxNumber import TaxNumber


@dataclass
class SupplierInfo:
    """Invoice supplier (seller) data

    :param supplier_tax_number: Tax number or group identification number, under which the supply of goods or services is done
    :param group_member_tax_number: Tax number of group member, when the supply of goods or services is done under group identification number
    :param community_vat_number: Community tax number
    :param supplier_name: Name of the seller (supplier)
    :param supplier_address: Address of the seller (supplier)
    :param supplier_bank_account_number: Bank account number of the seller (supplier)
    :param individual_exemption: Value is true if the seller (supplier) is individually exempted from VAT
    :param excise_licence_num: Number of supplier’s tax warehouse license or excise license (Act LXVIII of 2016)
    """

    supplier_tax_number: TaxNumber
    group_member_tax_number: Optional[TaxNumber]
    community_vat_number: Optional[str]
    supplier_name: str
    supplier_address: Address
    supplier_bank_account_number: Optional[str]
    individual_exemption: Optional[bool]
    excise_licence_num: Optional[str]
