from typing import Optional
from dataclasses import dataclass
from .ManageInvoiceOperation import ManageInvoiceOperation


@dataclass
class TransactionQueryParams:
    """Transactional params of the invoice query

    :param transaction_id: Transaction identifier of the data exchange
    :param index: Sequence number of the invoice within the request
    :param invoice_operation: Invoice operation type
    """

    transaction_id: str
    index: Optional[int]
    invoice_operation: Optional[ManageInvoiceOperation]
