from dataclasses import dataclass


@dataclass
class LineVatData:
    """Line VAT data

    :param line_vat_amount: VAT amount of the item expressed in the currency of the invoice
    :param line_vat_amount_huf: VAT amount of the item expressed in HUF
    """

    line_vat_amount: float
    line_vat_amount_huf: float
