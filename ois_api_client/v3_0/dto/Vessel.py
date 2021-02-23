from dataclasses import dataclass


@dataclass
class Vessel:
    """Data of vessel

    :param length: Length of hull in metre
    :param activity_referred: The value is true if the means of transport is exempt from VAT as per section 259 [25] (b)
    :param sailed_hours: Number of sailed hours
    """

    length: float
    activity_referred: bool
    sailed_hours: float
