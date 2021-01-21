from datetime import date
from typing import Optional, Union

from .Aircraft import Aircraft
from .Vehicle import Vehicle
from .Vessel import Vessel


class NewTransportMean:
    """Supply of new means of transport - section 89 § and 169 (o) of the VAT law

    :param vehicle_or_vessel_or_aircraft: Vehicle or Vessel or Aircraft data
    :param brand: Product / type
    :param serial_num: Chassis number / serial number / product number
    :param engine_num: Engine number
    :param first_entry_into_service: First entry into service
    """

    def __init__(self,
                 data: Union[Vehicle, Vessel, Aircraft],
                 brand: Optional[str] = None,
                 serial_num: Optional[str] = None,
                 engine_num: Optional[str] = None,
                 first_entry_into_service: Optional[date] = None):
        self.brand = brand
        self.serial_num = serial_num
        self.engine_num = engine_num
        self.first_entry_into_service = first_entry_into_service

        if isinstance(data, Vehicle):
            self.vehicle = data
        elif isinstance(data, Vessel):
            self.vessel = data
        elif isinstance(data, Aircraft):
            self.aircraft = data
