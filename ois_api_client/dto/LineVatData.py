class LineVatData:
    """Line VAT data

    :param line_vat_amount: VAT amount of the item expressed in the currency of the invoice
    :param line_vat_amount_huf: VAT amount of the item expressed in HUF
    """

    def __init__(self, line_vat_amount: float, line_vat_amount_huf: float):
        self.line_vat_amount = line_vat_amount
        self.line_vat_amount_huf = line_vat_amount_huf
