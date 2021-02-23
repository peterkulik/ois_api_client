from typing import Optional
from dataclasses import dataclass


@dataclass
class VatRate:
    """Marking tax rate or tax exempt supply

    :param vat_percentage: Applied tax rate - section 169 (j) of the VAT law
    :param vat_exemption: Marking tax exemption -  section 169 (m) of the VAT law
    :param vat_out_of_scope: Out of scope of the VAT law
    :param vat_domestic_reverse_charge: Marking the national is reverse charge taxation - section 142 of the VAT law
    :param margin_scheme_vat: Margin scheme including input tax
    :param margin_scheme_no_vat: Margin scheme not including input tax
    """

    vat_percentage: Optional[float]
    vat_exemption: Optional[str]
    vat_out_of_scope: Optional[bool]
    vat_domestic_reverse_charge: Optional[bool]
    margin_scheme_vat: Optional[bool]
    margin_scheme_no_vat: Optional[bool]
