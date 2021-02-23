from typing import Optional
from dataclasses import dataclass
from .InvoiceChainDigest import InvoiceChainDigest
from .InvoiceLines import InvoiceLines
from .InvoiceReferenceData import InvoiceReferenceData


@dataclass
class InvoiceChainElement:
    """Invoice chain element

    :param invoice_chain_digest: Invoice chain digest data
    :param invoice_lines: Product/service digest data appearing on the invoice or the modification document
    :param invoice_reference_data: Modification or cancellation data
    """

    invoice_chain_digest: InvoiceChainDigest
    invoice_lines: Optional[InvoiceLines]
    invoice_reference_data: Optional[InvoiceReferenceData]
