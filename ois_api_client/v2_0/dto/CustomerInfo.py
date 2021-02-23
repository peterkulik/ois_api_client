from typing import Optional
from dataclasses import dataclass
from .Address import Address
from .TaxNumber import TaxNumber


@dataclass
class CustomerInfo:
    """Customer data

    :param customer_tax_number: Tax number or group identification number, under which the purchase of goods or services is done
    :param group_member_tax_number: Tax number of group member, when the purchase of goods or services is done under group identification number
    :param community_vat_number: Community tax number
    :param third_state_tax_id: Third state tax identification number
    :param customer_name: Name of the customer
    :param customer_address: Address of the customer
    :param customer_bank_account_number: Bank account number of the customer
    """

    customer_tax_number: Optional[TaxNumber]
    group_member_tax_number: Optional[TaxNumber]
    community_vat_number: Optional[str]
    third_state_tax_id: Optional[str]
    customer_name: str
    customer_address: Address
    customer_bank_account_number: Optional[str]
