from typing import Optional
from dataclasses import dataclass
from .TaxNumber import TaxNumber


@dataclass
class CustomerTaxNumber(TaxNumber):
    """Tax number or group identification number, under which the purchase of goods or services is done

    :param group_member_tax_number: Tax number of group member, when the purchase of goods or services is done under group identification number
    """

    group_member_tax_number: Optional[TaxNumber]
