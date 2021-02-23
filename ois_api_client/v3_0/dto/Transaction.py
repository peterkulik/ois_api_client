from datetime import datetime
from dataclasses import dataclass
from .OriginalRequestVersion import OriginalRequestVersion
from .RequestStatus import RequestStatus
from .Source import Source


@dataclass
class Transaction:
    """Transaction query result

    :param ins_date: Insert date in UTC time
    :param ins_cus_user: Inserting user name
    :param source: Data exchange source
    :param transaction_id: Transaction ID of the invoice
    :param request_status: Processing status of the request
    :param technical_annulment: Indicates whether the transaction contains technical annulment
    :param original_request_version: requestVersion value of the invoice exchange
    :param item_count: Item count of the invoiceExchange
    """

    ins_date: datetime
    ins_cus_user: str
    source: Source
    transaction_id: str
    request_status: RequestStatus
    technical_annulment: bool
    original_request_version: OriginalRequestVersion
    item_count: int
