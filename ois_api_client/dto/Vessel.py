from decimal import Decimal


class Vessel:
    """Data of vessel

    :param length: Length of hull in metre
    :param activity_referred: The value is true if the means of transport is exempt from VAT as per section 259 [25] (b)
    :param sailed_hours: Number of sailed hours
    """

    def __init__(self, length: Decimal, activity_referred: bool, sailed_hours: Decimal):
        self.length = length
        self.activity_referred = activity_referred
        self.sailed_hours = sailed_hours
