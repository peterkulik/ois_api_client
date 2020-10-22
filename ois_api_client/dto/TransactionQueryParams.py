from typing import Union

from .ManageInvoiceOperation import ManageInvoiceOperation


class TransactionQueryParams:
    """Transactional params of the invoice query

    :param transaction_id: Transaction identifier of the data exchange
    :param index: Sequence number of the invoice within the request
    :param invoice_operation: Invoice operation type
    """

    def __init__(self,
                 transaction_id: str,
                 index: Union[int, None] = None,
                 invoice_operation: Union[ManageInvoiceOperation, None] = None):
        self.transaction_id = transaction_id
        self.index = index
        self.invoice_operation = invoice_operation
