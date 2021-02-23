from typing import Optional
from typing import List
from dataclasses import dataclass
from .InvoiceHead import InvoiceHead
from .InvoiceReference import InvoiceReference
from .Lines import Lines
from .ProductFeeSummary import ProductFeeSummary
from .Summary import Summary


@dataclass
class Invoice:
    """Data of a single invoice or modification document

    :param invoice_reference: Modification or cancellation data
    :param invoice_head: Data concerning the whole invoice
    :param invoice_lines: Product/service data appearing on the invoice
    :param product_fee_summary: Summary data of product charges
    :param invoice_summary: Summary data according to VAT law
    """

    invoice_reference: Optional[InvoiceReference]
    invoice_head: InvoiceHead
    invoice_lines: Optional[Lines]
    product_fee_summary: Optional[List[ProductFeeSummary]]
    invoice_summary: Summary
