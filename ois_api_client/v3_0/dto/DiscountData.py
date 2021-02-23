from typing import Optional
from dataclasses import dataclass


@dataclass
class DiscountData:
    """Discount data

    :param discount_description: Description of the discount
    :param discount_value: Total amount of discount per item expressed in the currency of the invoice if not included in the unit price
    :param discount_rate: Rate of discount per item expressed in the currency of the invoice if not included in the unit price
    """

    discount_description: Optional[str]
    discount_value: Optional[float]
    discount_rate: Optional[float]
