from typing import Optional
from dataclasses import dataclass
from .CustomerTaxNumber import CustomerTaxNumber


@dataclass
class CustomerVatData:
    """VAT subjectivity data of the customer

    :param customer_tax_number: Domestic tax number or group identification number, under which the purchase of goods or services is done
    :param community_vat_number: Community tax number
    :param third_state_tax_id: Third state tax identification number
    """

    customer_tax_number: Optional[CustomerTaxNumber]
    community_vat_number: Optional[str]
    third_state_tax_id: Optional[str]
