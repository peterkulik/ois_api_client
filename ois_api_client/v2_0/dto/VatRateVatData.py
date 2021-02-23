from dataclasses import dataclass


@dataclass
class VatRateVatData:
    """VAT data of given tax rate

    :param vat_rate_vat_amount: VAT amount of sales or service delivery under a given tax rate expressed in the currency of the invoice
    :param vat_rate_vat_amount_huf: VAT amount of sales or service delivery under a given tax rate expressed in HUF
    """

    vat_rate_vat_amount: float
    vat_rate_vat_amount_huf: float
