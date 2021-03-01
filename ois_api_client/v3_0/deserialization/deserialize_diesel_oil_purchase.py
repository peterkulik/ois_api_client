from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import BASE
from ..namespaces import COMMON
from ..namespaces import DATA
from ..dto.DieselOilPurchase import DieselOilPurchase
from .deserialize_simple_address import deserialize_simple_address


def deserialize_diesel_oil_purchase(element: ET.Element) -> Optional[DieselOilPurchase]:
    if element is None:
        return None

    result = DieselOilPurchase(
        purchase_location=deserialize_simple_address(
            XR.find_child(element, 'purchaseLocation', DATA)
        ),
        purchase_date=XR.get_child_date(element, 'purchaseDate', DATA),
        vehicle_registration_number=XR.get_child_text(element, 'vehicleRegistrationNumber', DATA),
        diesel_oil_quantity=XR.get_child_float(element, 'dieselOilQuantity', DATA),
    )

    return result
