from dataclasses import dataclass
from .VatRate import VatRate


@dataclass
class LineAmountsSimplified:
    """Item value data to be completed in case of simplified invoice

    :param line_vat_rate: Tax rate or tax exemption marking
    :param line_gross_amount_simplified: Gross amount of the item expressed in the currency of the invoice
    :param line_gross_amount_simplified_huf: Gross amount of the item expressed in HUF
    """

    line_vat_rate: VatRate
    line_gross_amount_simplified: float
    line_gross_amount_simplified_huf: float
