from typing import Optional
from dataclasses import dataclass


@dataclass
class LineAmountsSimplified:
    """Item value data to be completed in case of simplified invoice

    :param line_vat_content: VAT content of the item, in case of simplified invoice
    :param line_gross_amount_simplified: Gross amount of the item expressed in the currency of the invoice
    :param line_gross_amount_simplified_huf: Gross amount of the item expressed in HUF
    """

    line_vat_content: Optional[float]
    line_gross_amount_simplified: float
    line_gross_amount_simplified_huf: float
