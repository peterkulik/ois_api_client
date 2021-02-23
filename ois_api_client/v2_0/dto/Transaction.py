from datetime import datetime
from dataclasses import dataclass
from .OriginalRequestVersion import OriginalRequestVersion
from .Source import Source


@dataclass
class Transaction:
    """Transaction query result

    :param ins_date: Insert date in UTC time
    :param ins_cus_user: Inserting user name
    :param source: Data exchange source
    :param transaction_id: Transaction ID of the invoice
    :param original_request_version: None
    :param item_count: Item count of the invoiceExchange
    """

    ins_date: datetime
    ins_cus_user: str
    source: Source
    transaction_id: str
    original_request_version: OriginalRequestVersion
    item_count: int
