from dataclasses import dataclass
from .TransactionListResult import TransactionListResult
from .BasicOnlineInvoiceResponse import BasicOnlineInvoiceResponse


@dataclass
class QueryTransactionListResponse(BasicOnlineInvoiceResponse):
    """Response type of the POST /queryTransactionList REST operation

    :param transaction_list_result: Transaction query results
    """

    transaction_list_result: TransactionListResult
