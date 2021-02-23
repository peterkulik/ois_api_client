from typing import Optional
from dataclasses import dataclass
from .Crypto import Crypto
from .ManageInvoiceOperation import ManageInvoiceOperation


@dataclass
class InvoiceOperation:
    """Invoice operation of the request

    :param index: Sequence number of the invoice within the request
    :param invoice_operation: Type of the desired invoice operation
    :param invoice_data: Invoice data in BASE64 encoded form
    :param electronic_invoice_hash: Electronic invoice or modification document file hash value
    """

    index: int
    invoice_operation: ManageInvoiceOperation
    invoice_data: str
    electronic_invoice_hash: Optional[Crypto]
