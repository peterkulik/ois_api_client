from typing import Optional
from dataclasses import dataclass
from .BasicOnlineInvoiceRequest import BasicOnlineInvoiceRequest


@dataclass
class QueryTransactionStatusRequest(BasicOnlineInvoiceRequest):
    """Request type of the POST /queryTransactionStatus REST operation

    :param transaction_id: Transaction identifier of the data exchange
    :param return_original_request: Indicates if the original client data should also be returned in the response
    """

    transaction_id: str
    return_original_request: Optional[bool]
