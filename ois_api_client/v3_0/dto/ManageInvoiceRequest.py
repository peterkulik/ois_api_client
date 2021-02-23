from dataclasses import dataclass
from .InvoiceOperationList import InvoiceOperationList
from .BasicOnlineInvoiceRequest import BasicOnlineInvoiceRequest


@dataclass
class ManageInvoiceRequest(BasicOnlineInvoiceRequest):
    """Request type of the POST /manageInvoice REST operation

    :param exchange_token: The decoded unique token issued for the current transaction
    :param invoice_operations: Batch invoice operations of the request
    """

    exchange_token: str
    invoice_operations: InvoiceOperationList
