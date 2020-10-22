class Vessel:
    """Data of vessel

    :param length: Length of hull in metre
    :param sailed_hours: Number of sailed hours
    :param activity_referred: The value is true if the means of transport is exempt from VAT as per section 259 [25] (b)
    """

    def __init__(self,
                 length: float,
                 sailed_hours: float,
                 activity_referred: bool = False):
        self.length = length
        self.activity_referred = activity_referred
        self.sailed_hours = sailed_hours
