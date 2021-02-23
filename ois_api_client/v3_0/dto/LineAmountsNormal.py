from typing import Optional
from dataclasses import dataclass
from .LineGrossAmountData import LineGrossAmountData
from .LineNetAmountData import LineNetAmountData
from .LineVatData import LineVatData
from .VatRate import VatRate


@dataclass
class LineAmountsNormal:
    """Item value data to be completed in case of normal or aggregate invoice

    :param line_net_amount_data: Line net data
    :param line_vat_rate: Tax rate or tax exemption marking
    :param line_vat_data: Line VAT data
    :param line_gross_amount_data: Line gross data
    """

    line_net_amount_data: LineNetAmountData
    line_vat_rate: VatRate
    line_vat_data: Optional[LineVatData]
    line_gross_amount_data: Optional[LineGrossAmountData]
