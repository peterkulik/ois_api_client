class Vehicle:
    """Other data in relation to motorised land vehicle

    :param engine_capacity: Engine capacity in cubic centimetre
    :param engine_power: Engine power in kW
    :param kms: Travelled distance in km
    """

    def __init__(self, engine_capacity: float, engine_power: float, kms: float):
        self.engine_capacity = engine_capacity
        self.engine_power = engine_power
        self.kms = kms
