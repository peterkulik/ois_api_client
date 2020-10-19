from datetime import date
from typing import Union

from .Aircraft import Aircraft
from .Vehicle import Vehicle
from .Vessel import Vessel


class NewTransportMean:
    """Supply of new means of transport - section 89 § and 169 (o) of the VAT law

    :param brand: Product / type
    :param serial_num: Chassis number / serial number / product number
    :param engine_num: Engine number
    :param first_entry_into_service: First entry into service
    :param vehicle_or_vessel_or_aircraft: Vehicle or Vessel or Aircraft data
    """

    def __init__(self, brand: str, serial_num: str, engine_num: str, first_entry_into_service: date,
                 vehicle_or_vessel_or_aircraft: Union[Vehicle, Vessel, Aircraft]):
        self.brand = brand
        self.serial_num = serial_num
        self.engine_num = engine_num
        self.first_entry_into_service = first_entry_into_service
        self.vehicle_or_vessel_or_aircraft = vehicle_or_vessel_or_aircraft
