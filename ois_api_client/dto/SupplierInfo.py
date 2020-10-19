from typing import Union

from .DetailedAddress import DetailedAddress
from .SimpleAddress import SimpleAddress
from .TaxNumber import TaxNumber


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

    def __init__(self, supplier_tax_number: TaxNumber, group_member_tax_number: TaxNumber, community_vat_number: str,
                 supplier_name: str, supplier_address: Union[SimpleAddress, DetailedAddress],
                 supplier_bank_account_number: str, individual_exemption: bool, excise_licence_num: str):
        self.supplier_tax_number = supplier_tax_number
        self.group_member_tax_number = group_member_tax_number
        self.community_vat_number = community_vat_number
        self.supplier_name = supplier_name
        self.supplier_address = supplier_address
        self.supplier_bank_account_number = supplier_bank_account_number
        self.individual_exemption = individual_exemption
        self.excise_licence_num = excise_licence_num
