class VatRateVatData:
    """VAT data of given tax rate

    vat_rate_vat_amount: VAT amount of sales or service delivery under a given tax rate expressed in the currency of the invoice
    vat_rate_vat_amount_huf: VAT amount of sales or service delivery under a given tax rate expressed in HUF
    """

    def __init__(self, vat_rate_vat_amount: float, vat_rate_vat_amount_huf: float):
        self.vat_rate_vat_amount = vat_rate_vat_amount
        self.vat_rate_vat_amount_huf = vat_rate_vat_amount_huf
