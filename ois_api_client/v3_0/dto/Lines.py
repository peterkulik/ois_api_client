from typing import List
from dataclasses import dataclass
from .Line import Line


@dataclass
class Lines:
    """Product / service items

    :param merged_item_indicator: Indicates whether the data exchange contains merged line data due to size reduction
    :param line: Product / service item
    """

    merged_item_indicator: bool
    line: List[Line]
