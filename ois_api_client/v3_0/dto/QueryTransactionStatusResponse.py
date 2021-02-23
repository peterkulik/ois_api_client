from typing import Optional
from dataclasses import dataclass
from .ProcessingResultList import ProcessingResultList
from .BasicOnlineInvoiceResponse import BasicOnlineInvoiceResponse


@dataclass
class QueryTransactionStatusResponse(BasicOnlineInvoiceResponse):
    """Response type of the POST /queryTransactionStatus REST operation

    :param processing_results: Processing status of the invoices in the request
    """

    processing_results: Optional[ProcessingResultList]
