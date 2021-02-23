from typing import Optional
from dataclasses import dataclass
from .Address import Address
from .CustomerVatData import CustomerVatData
from .CustomerVatStatus import CustomerVatStatus


@dataclass
class CustomerInfo:
    """Customer data

    :param customer_vat_status: Customers status by VAT
    :param customer_vat_data: VAT subjectivity data of the customer
    :param customer_name: Name of the customer
    :param customer_address: Address of the customer
    :param customer_bank_account_number: Bank account number of the customer
    """

    customer_vat_status: CustomerVatStatus
    customer_vat_data: Optional[CustomerVatData]
    customer_name: Optional[str]
    customer_address: Optional[Address]
    customer_bank_account_number: Optional[str]
