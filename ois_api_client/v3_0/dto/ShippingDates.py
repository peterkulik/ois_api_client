from typing import List
from dataclasses import dataclass


@dataclass
class ShippingDates:
    """Shipping dates

    :param shipping_date: Shipping date
    """

    shipping_date: List[str]
