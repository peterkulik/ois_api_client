from dataclasses import dataclass
from .BasicResponse import BasicResponse


@dataclass
class TransactionResponse(BasicResponse):
    """Common response type of the POST /manageInvoice and the POST /manageAnnulment REST operation

    :param transaction_id: Transaction identifier of the requested operation
    """

    transaction_id: str
