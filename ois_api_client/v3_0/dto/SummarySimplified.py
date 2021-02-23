from dataclasses import dataclass
from .VatRate import VatRate


@dataclass
class SummarySimplified:
    """Calculation of simplified invoice totals

    :param vat_rate: Marking the tax rate or the fact of tax exemption
    :param vat_content_gross_amount: The gross amount of the sale or service for the given tax amount in the currency of the invoice
    :param vat_content_gross_amount_huf: The gross amount of the sale or service for the given tax amount in HUF
    """

    vat_rate: VatRate
    vat_content_gross_amount: float
    vat_content_gross_amount_huf: float
