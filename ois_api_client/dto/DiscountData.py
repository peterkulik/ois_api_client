class DiscountData:
    """Discount data
    :param discount_description: Description of the discount
    :param discount_value: Total amount of discount per item expressed in the currency of the invoice if not included in the unit price
    :param discount_rate: Rate of discount per item expressed in the currency of the invoice if not included in the unit price
    """

    def __init__(self, discount_description: str, discount_value: float, discount_rate: float):
        self.discount_description = discount_description
        self.discount_value = discount_value
        self.discount_rate = discount_rate
