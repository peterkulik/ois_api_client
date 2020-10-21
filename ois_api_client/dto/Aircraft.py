class Aircraft:
    """Aircraft

    :param take_off_weight: Take-off weight in kilogram
    :param air_cargo: The value is true if the means of transport is exempt from VAT as per section 259 [25] (c)
    :param operation_hours: Number of aviated hours
    """

    def __init__(self, take_off_weight: float, air_cargo: bool, operation_hours: float):
        self.take_off_weight = take_off_weight
        self.air_cargo = air_cargo
        self.operation_hours = operation_hours
