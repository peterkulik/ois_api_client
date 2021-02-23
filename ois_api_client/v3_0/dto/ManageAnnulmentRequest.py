from dataclasses import dataclass
from .AnnulmentOperationList import AnnulmentOperationList
from .BasicOnlineInvoiceRequest import BasicOnlineInvoiceRequest


@dataclass
class ManageAnnulmentRequest(BasicOnlineInvoiceRequest):
    """Request type of the POST /manageAnnulment REST operation

    :param exchange_token: The decoded unique token issued for the current transaction
    :param annulment_operations: Batch technical annulment operations of the request
    """

    exchange_token: str
    annulment_operations: AnnulmentOperationList
