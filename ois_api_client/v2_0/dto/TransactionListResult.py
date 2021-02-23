from typing import Optional
from typing import List
from dataclasses import dataclass
from .Transaction import Transaction


@dataclass
class TransactionListResult:
    """Transaction query results

    :param current_page: The currently queried page count
    :param available_page: The highest available page count matching the query
    :param transaction: Transaction query result
    """

    current_page: int
    available_page: int
    transaction: Optional[List[Transaction]]
