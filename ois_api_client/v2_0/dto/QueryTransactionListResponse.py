from dataclasses import dataclass
from .TransactionListResult import TransactionListResult
from .BasicResponse import BasicResponse


@dataclass
class QueryTransactionListResponse(BasicResponse):
    """Response type of the POST /queryTransactionList REST operation

    :param transaction_list_result: Transaction query results
    """

    transaction_list_result: TransactionListResult
