class LineNetAmountData:
    """Line net data

    :param line_net_amount: Net amount of the item expressed in the currency of the invoice. In case of margin scheme
    taxation containing VAT, the amount of consideration reduced with the amount of VAT, expressed in the currency of
    the invoice.
    :param line_net_amount_huf: Net amount of the item expressed in HUF. Net amount of the item
    expressed in the currency of the invoice. In case of margin scheme taxation containing VAT, the amount of
    consideration reduced with the amount of VAT, expressed in HUF.
    """

    def __init__(
            self,
            line_net_amount: float,
            line_net_amount_huf: float):
        self.line_net_amount = line_net_amount
        self.line_net_amount_huf = line_net_amount_huf
