from typing import Optional
from dataclasses import dataclass
from .DetailedReason import DetailedReason
from .MarginScheme import MarginScheme
from .VatAmountMismatch import VatAmountMismatch


@dataclass
class VatRate:
    """Marking tax rate or tax exempt supply

    :param vat_percentage: Applied tax rate - section 169 (j) of the VAT law
    :param vat_content: VAT content in case of simplified invoice
    :param vat_exemption: Marking tax exemption -  section 169 (m) of the VAT law
    :param vat_out_of_scope: Out of scope of the VAT law
    :param vat_domestic_reverse_charge: Marking the national is reverse charge taxation - section 142 of the VAT law
    :param margin_scheme_indicator: Marking the margin-scheme taxation as per section 169 (p)(q)
    :param vat_amount_mismatch: Different cases of mismatching tax base and levied tax
    :param no_vat_charge: No VAT charged under Section 17
    """

    vat_percentage: Optional[float]
    vat_content: Optional[float]
    vat_exemption: Optional[DetailedReason]
    vat_out_of_scope: Optional[DetailedReason]
    vat_domestic_reverse_charge: Optional[bool]
    margin_scheme_indicator: Optional[MarginScheme]
    vat_amount_mismatch: Optional[VatAmountMismatch]
    no_vat_charge: Optional[bool]
