from typing import Optional
from dataclasses import dataclass
from .Takeover import Takeover


@dataclass
class ProductFeeTakeoverData:
    """Data in connection with takeover of environmental protection product fee

    :param takeover_reason: Direction and legal base of takeover
    :param takeover_amount: Amount in Hungarian forints of the product fee taken over if the purchaser takes over the supplier’s product fee liability
    """

    takeover_reason: Takeover
    takeover_amount: Optional[float]
