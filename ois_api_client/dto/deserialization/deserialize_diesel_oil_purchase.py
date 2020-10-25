import xml.etree.ElementTree as ET
from typing import Union

from .XmlReader import XmlReader as XR
from .deserialize_simple_address import deserialize_simple_address
from ..DieselOilPurchase import DieselOilPurchase
from ...constants import NAMESPACE_DATA


def deserialize_diesel_oil_purchase(element: ET.Element) -> Union[DieselOilPurchase, None]:
    if element is None:
        return None

    result = DieselOilPurchase(
        purchase_location=deserialize_simple_address(XR.find_child('purchaseLocation')),
        purchase_date=XR.get_child_date(element, 'purchaseDate', NAMESPACE_DATA),
        vehicle_registration_number=XR.get_child_text(element, 'vehicleRegistrationNumber', NAMESPACE_DATA),
        diesel_oil_quantity=XR.get_child_float(element, 'dieselOilQuantity', NAMESPACE_DATA)
    )

    return result
