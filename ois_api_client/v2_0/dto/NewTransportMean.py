from typing import Optional
from datetime import date
from dataclasses import dataclass
from .Aircraft import Aircraft
from .Vehicle import Vehicle
from .Vessel import Vessel


@dataclass
class NewTransportMean:
    """Supply of new means of transport - section 89 § and 169 (o) of the VAT law

    :param brand: Product / type
    :param serial_num: Chassis number / serial number / product number
    :param engine_num: Engine number
    :param first_entry_into_service: First entry into service
    :param vehicle: Other data in relation to motorised land vehicle
    :param vessel: Data of vessel
    :param aircraft: Aircraft
    """

    brand: Optional[str]
    serial_num: Optional[str]
    engine_num: Optional[str]
    first_entry_into_service: date
    vehicle: Vehicle
    vessel: Vessel
    aircraft: Aircraft
