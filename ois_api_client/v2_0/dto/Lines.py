from typing import List
from dataclasses import dataclass
from .Line import Line


@dataclass
class Lines:
    """Product / service items

    :param line: Product / service item
    """

    line: List[Line]
