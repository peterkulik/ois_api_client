from typing import Union

from .Address import Address
from .TaxNumber import TaxNumber


class CustomerInfo:
    """Customer data

    :param customer_name: >Name of the customer
    :param customer_address: Address of the customer
    :param customer_tax_number: Tax number or group identification number, under which the purchase of goods or services is done
    :param group_member_tax_number: Tax number of group member, when the purchase of goods or services is done under group identification number
    :param community_vat_number: Community tax number
    :param third_state_tax_id: Third state tax identification number
    :param customer_bank_account_number: Bank account number of the customer
    """

    def __init__(self,
                 customer_name: str,
                 customer_address: Address,
                 customer_tax_number: Union[TaxNumber, None] = None,
                 group_member_tax_number: Union[TaxNumber, None] = None,
                 community_vat_number: Union[str, None] = None,
                 third_state_tax_id: Union[str, None] = None,
                 customer_bank_account_number: Union[str, None] = None):
        self.customer_tax_number = customer_tax_number
        self.group_member_tax_number = group_member_tax_number
        self.community_vat_number = community_vat_number
        self.third_state_tax_id = third_state_tax_id
        self.customer_name = customer_name
        self.customer_address = customer_address
        self.customer_bank_account_number = customer_bank_account_number
