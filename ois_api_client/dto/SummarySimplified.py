class SummarySimplified:
    """Calculation of simplified invoice totals
    :param vat_content: In the case of a simplified invoice, VAT content rate
    :param vat_content_gross_amount: The gross amount of the sale or service for the given tax amount in the currency of the invoice
    :param vat_content_gross_amount_huf: The gross amount of the sale or service for the given tax amount in HUF
    """

    def __init__(self,
                 vat_content: float,
                 vat_content_gross_amount: float,
                 vat_content_gross_amount_huf: float):
        self.vat_content = vat_content
        self.vat_content_gross_amount = vat_content_gross_amount
        self.vat_content_gross_amount_huf = vat_content_gross_amount_huf
