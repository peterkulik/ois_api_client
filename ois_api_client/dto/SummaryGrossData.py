class SummaryGrossData:
    """Gross data of the invoice summary

    :param invoice_gross_amount: Gross amount of the invoice expressed in the currency of the invoice
    :param invoice_gross_amount_huf: Gross amount of the invoice expressed in HUF
    """

    def __init__(self,
                 invoice_gross_amount: float,
                 invoice_gross_amount_huf: float):
        self.invoice_gross_amount = invoice_gross_amount
        self.invoice_gross_amount_huf = invoice_gross_amount_huf
