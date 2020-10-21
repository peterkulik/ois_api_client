class VatRateNetData:
    """Net data of given tax rate

    :param vat_rate_net_amount: Net amount of sales or service delivery under a given tax rate expressed in the currency of the invoice
    :param vat_rate_net_amount_huf: Net amount of sales or service delivery under a given tax rate expressed in HUF
    """

    def __init__(self, vat_rate_net_amount: float, vat_rate_net_amount_huf: float):
        self.vat_rate_net_amount = vat_rate_net_amount
        self.vat_rate_net_amount_huf = vat_rate_net_amount_huf
