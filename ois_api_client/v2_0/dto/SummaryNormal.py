from typing import List
from dataclasses import dataclass
from .SummaryByVatRate import SummaryByVatRate


@dataclass
class SummaryNormal:
    """Calculation of invoice totals (not simplified invoice)

    :param summary_by_vat_rate: Calculation of invoice totals per VAT rates
    :param invoice_net_amount: Net amount of the invoice expressed in the currency of the invoice
    :param invoice_net_amount_huf: Net amount of the invoice expressed in HUF
    :param invoice_vat_amount: VAT amount of the invoice expressed in the currency of the invoice
    :param invoice_vat_amount_huf: VAT amount of the invoice expressed in HUF
    """

    summary_by_vat_rate: List[SummaryByVatRate]
    invoice_net_amount: float
    invoice_net_amount_huf: float
    invoice_vat_amount: float
    invoice_vat_amount_huf: float
