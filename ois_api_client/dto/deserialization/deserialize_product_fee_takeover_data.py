import xml.etree.ElementTree as ET
from typing import Union

from .XmlReader import XmlReader as XR
from ..ProductFeeTakeoverData import ProductFeeTakeoverData
from ..Takeover import Takeover
from ...constants import NAMESPACE_DATA


def deserialize_product_fee_takeover_data(element: ET.Element) -> Union[ProductFeeTakeoverData, None]:
    if element is None:
        return None

    takeover = XR.get_child_text(element, 'takeoverReason', NAMESPACE_DATA)

    result = ProductFeeTakeoverData(
        takeover_reason=Takeover(takeover) if takeover is not None else None,
        takeover_amount=XR.get_child_float(element, 'takeoverAmount', NAMESPACE_DATA)
    )

    return result
