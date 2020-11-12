from typing import Optional

from .Address import Address
from .CustomerVatData import CustomerVatData


class CustomerInfo:
    """Customer data

    :param private_person_indicator: Customer's private person indicator
    :param customer_vat_data: VAT subjectivity data of the customer
    :param customer_name: Name of the customer
    :param customer_address: Address of the customer
    :param customer_bank_account_number: Bank account number of the customer
    """

    def __init__(self,
                 private_person_indicator: bool,
                 customer_vat_data: Optional[CustomerVatData] = None,
                 customer_name: Optional[str] = None,
                 customer_address: Optional[Address] = None,
                 customer_bank_account_number: Optional[str] = None):
        self.private_person_indicator = private_person_indicator
        self.customer_vat_data = customer_vat_data
        self.customer_name = customer_name
        self.customer_address = customer_address
        self.customer_bank_account_number = customer_bank_account_number
