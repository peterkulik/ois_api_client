from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import BASE
from ..namespaces import DATA
from ...deserialization.create_enum import create_enum
from ..dto.ProductFeeTakeoverData import ProductFeeTakeoverData
from ..dto.Takeover import Takeover


def deserialize_product_fee_takeover_data(element: ET.Element) -> Optional[ProductFeeTakeoverData]:
    if element is None:
        return None

    result = ProductFeeTakeoverData(
        takeover_reason=create_enum(Takeover, XR.get_child_text(element, 'takeoverReason', DATA)),
        takeover_amount=XR.get_child_float(element, 'takeoverAmount', DATA),
    )

    return result
