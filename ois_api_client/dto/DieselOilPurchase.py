from datetime import date
from typing import Union

from .SimpleAddress import SimpleAddress


class DieselOilPurchase:
    """Data of gas oil acquisition after taxation – point a), paragraph (1) of Section 75 of the NGM Decree No. 45

    :param purchase_location: Place of purchase of the gas oil
    :param purchase_date: Date of purchase of gas oil
    :param vehicle_registration_number: Registration number of vehicle (letters and numbers only)
    :param diesel_oil_quantity: Quantity of diesel oil used for contract work and machinery hire service in liter – Act LXVIII of 2016 on Excise Tax section 117 (2)
    """

    def __init__(self,
                 purchase_location: SimpleAddress,
                 purchase_date: date,
                 vehicle_registration_number: str,
                 diesel_oil_quantity: Union[float, None] = None):
        self.purchase_location = purchase_location
        self.purchase_date = purchase_date
        self.vehicle_registration_number = vehicle_registration_number
        self.diesel_oil_quantity = diesel_oil_quantity
