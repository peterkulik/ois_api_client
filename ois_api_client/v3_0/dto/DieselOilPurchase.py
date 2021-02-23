from typing import Optional
from datetime import date
from dataclasses import dataclass
from .SimpleAddress import SimpleAddress


@dataclass
class DieselOilPurchase:
    """Data of gas oil acquisition after taxation – point a), paragraph (1) of Section 75 of the NGM Decree No. 45/2016. (XI. 29.)

    :param purchase_location: Place of purchase of the gas oil
    :param purchase_date: Date of purchase of gas oil
    :param vehicle_registration_number: Registration number of vehicle (letters and numbers only)
    :param diesel_oil_quantity: Fordítandó helyett: Quantity of diesel oil used for contract work and machinery hire service in liter – Act LXVIII of 2016 on Excise Tax section 117 (2)
    """

    purchase_location: SimpleAddress
    purchase_date: date
    vehicle_registration_number: str
    diesel_oil_quantity: Optional[float]
