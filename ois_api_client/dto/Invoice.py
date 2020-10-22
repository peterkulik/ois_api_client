from typing import Union, List

from .InvoiceHead import InvoiceHead
from .InvoiceReference import InvoiceReference
from .Lines import Lines
from .ProductFeeSummary import ProductFeeSummary
from .Summary import Summary


class Invoice:
    """Data of a single invoice or modification document

    :param invoice_head: Data concerning the whole invoice
    :param invoice_summary: Summary data according to VAT law
    :param invoice_reference: Modification or cancellation data
    :param invoice_lines: Product/service data appearing on the invoice
    :param product_fee_summary: Summary data of product charges
    """

    def __init__(self,
                 invoice_head: InvoiceHead,
                 invoice_summary: Summary,
                 invoice_reference: Union[InvoiceReference, None] = None,
                 invoice_lines: Union[Lines, None] = None,
                 product_fee_summary: Union[List[ProductFeeSummary], None] = None):
        self.invoice_reference = invoice_reference
        self.invoice_head = invoice_head
        self.invoice_lines = invoice_lines
        self.product_fee_summary = product_fee_summary
        self.invoice_summary = invoice_summary
