from dataclasses import dataclass
from .InvoiceOperationList import InvoiceOperationList
from .BasicRequest import BasicRequest


@dataclass
class ManageInvoiceRequest(BasicRequest):
    """Request type of the POST /manageInvoice REST operation

    :param exchange_token: The decoded unique token issued for the current transaction
    :param invoice_operations: Batch invoice operations of the request
    """

    exchange_token: str
    invoice_operations: InvoiceOperationList
