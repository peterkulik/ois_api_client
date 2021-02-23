from typing import List
from dataclasses import dataclass


@dataclass
class OrderNumbers:
    """Order numbers

    :param order_number: Order number
    """

    order_number: List[str]
