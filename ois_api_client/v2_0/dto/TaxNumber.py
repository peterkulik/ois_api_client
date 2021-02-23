from typing import Optional
from dataclasses import dataclass


@dataclass
class TaxNumber:
    """Tax number type

    :param taxpayer_id: Core tax number of the taxable person. In case of group taxation arrangement the group identification number
    :param vat_code: VAT code to indicate taxation type of the taxpayer. One digit
    :param county_code: County code, two digits
    """

    taxpayer_id: str
    vat_code: Optional[str]
    county_code: Optional[str]
