class LineGrossAmountData:
    """Line gross data

    :param line_gross_amount_normal: Gross amount of the item expressed in the currency of the invoice. In case of
    margin scheme taxation containing VAT, the amount of consideration expressed in the currency of the invoice.
    :param line_gross_amount_normal_huf: Gross amount of the item expressed in HUF
    """

    def __init__(self,
                 line_gross_amount_normal: float,
                 line_gross_amount_normal_huf: float):
        self.line_gross_amount_normal = line_gross_amount_normal
        self.line_gross_amount_normal_huf = line_gross_amount_normal_huf
