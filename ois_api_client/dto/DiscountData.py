from typing import Optional


class DiscountData:
    """Discount data
    :param discount_description: Description of the discount
    :param discount_value: Total amount of discount per item expressed in the currency of the invoice if not included in the unit price
    :param discount_rate: Rate of discount per item expressed in the currency of the invoice if not included in the unit price
    """

    def __init__(self,
                 discount_description: Optional[str] = None,
                 discount_value: Optional[float] = None,
                 discount_rate: Optional[float] = None):
        self.discount_description = discount_description
        self.discount_value = discount_value
        self.discount_rate = discount_rate
