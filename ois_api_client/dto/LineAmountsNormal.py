from typing import Union

from .LineGrossAmountData import LineGrossAmountData
from .LineNetAmountData import LineNetAmountData
from .LineVatData import LineVatData
from .VatRate import VatRate


class LineAmountsNormal:
    """Item value data to be completed in case of normal or aggregate invoice

    :param line_net_amount_data: Line net data
    :param line_vat_rate: Tax rate or tax exemption marking
    :param line_vat_data: Line VAT data
    :param line_gross_amount_data: Line gross data
    """

    def __init__(self,
                 line_net_amount_data: LineNetAmountData,
                 line_vat_rate: VatRate,
                 line_vat_data: Union[LineVatData, None] = None,
                 line_gross_amount_data: Union[LineGrossAmountData, None] = None):
        self.line_net_amount_data = line_net_amount_data
        self.line_vat_rate = line_vat_rate
        self.line_vat_data = line_vat_data
        self.line_gross_amount_data = line_gross_amount_data
