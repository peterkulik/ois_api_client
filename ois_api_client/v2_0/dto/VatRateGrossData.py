from dataclasses import dataclass


@dataclass
class VatRateGrossData:
    """Gross data of given tax rate

    :param vat_rate_gross_amount: Gross amount of sales or service delivery under a given tax rate expressed in the currency of the invoice
    :param vat_rate_gross_amount_huf: Gross amount of sales or service delivery under a given tax rate expressed in HUF
    """

    vat_rate_gross_amount: float
    vat_rate_gross_amount_huf: float
