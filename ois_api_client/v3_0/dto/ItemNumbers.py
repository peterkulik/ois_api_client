from typing import List
from dataclasses import dataclass


@dataclass
class ItemNumbers:
    """Item numbers

    :param item_number: Item number
    """

    item_number: List[str]
