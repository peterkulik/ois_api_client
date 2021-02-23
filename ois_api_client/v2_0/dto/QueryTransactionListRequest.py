from dataclasses import dataclass
from .DateTimeIntervalParam import DateTimeIntervalParam
from .BasicRequest import BasicRequest


@dataclass
class QueryTransactionListRequest(BasicRequest):
    """Request type of the POST /queryTransactionList REST operation

    :param page: The queried page count
    :param ins_date: The queried transaction's insert date on server side in UTC time
    """

    page: int
    ins_date: DateTimeIntervalParam
