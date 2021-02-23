from typing import Optional
from dataclasses import dataclass
from .DateTimeIntervalParam import DateTimeIntervalParam
from .RequestStatus import RequestStatus
from .BasicOnlineInvoiceRequest import BasicOnlineInvoiceRequest


@dataclass
class QueryTransactionListRequest(BasicOnlineInvoiceRequest):
    """Request type of the POST /queryTransactionList REST operation

    :param page: The queried page count
    :param ins_date: The queried transaction's insert date on server side in UTC time
    :param request_status: Processing status of the request
    """

    page: int
    ins_date: DateTimeIntervalParam
    request_status: Optional[RequestStatus]
