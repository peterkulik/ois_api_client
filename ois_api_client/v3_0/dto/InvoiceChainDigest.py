from typing import Optional
from datetime import datetime
from dataclasses import dataclass
from .ManageInvoiceOperation import ManageInvoiceOperation
from .OriginalRequestVersion import OriginalRequestVersion


@dataclass
class InvoiceChainDigest:
    """Invoice chain digest data

    :param invoice_number: Sequential number of the original invoice or modification document - section 169 (b) or section 170 (1) b) of the VAT law
    :param batch_index: Sequence number of the modification document within the batch
    :param invoice_operation: Invoice operation type
    :param supplier_tax_number: The supplier's tax number
    :param customer_tax_number: The buyer's tax number
    :param ins_date: Insert date in UTC time
    :param original_request_version: requestVersion value of the invoice exchange
    """

    invoice_number: str
    batch_index: Optional[int]
    invoice_operation: ManageInvoiceOperation
    supplier_tax_number: str
    customer_tax_number: Optional[str]
    ins_date: datetime
    original_request_version: OriginalRequestVersion
