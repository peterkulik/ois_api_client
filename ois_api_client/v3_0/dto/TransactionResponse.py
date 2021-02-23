from dataclasses import dataclass
from .BasicOnlineInvoiceResponse import BasicOnlineInvoiceResponse


@dataclass
class TransactionResponse(BasicOnlineInvoiceResponse):
    """Common response type of the POST /manageInvoice and the POST /manageAnnulment REST operation

    :param transaction_id: Transaction identifier of the requested operation
    """

    transaction_id: str
