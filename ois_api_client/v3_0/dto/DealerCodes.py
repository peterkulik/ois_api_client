from typing import List
from dataclasses import dataclass


@dataclass
class DealerCodes:
    """Dealer codes

    :param dealer_code: Dealer code
    """

    dealer_code: List[str]
