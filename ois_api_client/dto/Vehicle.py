from decimal import Decimal


class Vehicle:
    """Other data in relation to motorised land vehicle

    :param engine_capacity: Engine capacity in cubic centimetre
    :param engine_power: Engine power in kW
    :param kms: Travelled distance in km
    """

    def __init__(self, engine_capacity: Decimal, engine_power: Decimal, kms: Decimal):
        self.engine_capacity = engine_capacity
        self.engine_power = engine_power
        self.kms = kms
