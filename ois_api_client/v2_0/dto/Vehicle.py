from dataclasses import dataclass


@dataclass
class Vehicle:
    """Other data in relation to motorised land vehicle

    :param engine_capacity: Engine capacity in cubic centimetre
    :param engine_power: Engine power in kW
    :param kms: Travelled distance in km
    """

    engine_capacity: float
    engine_power: float
    kms: float
