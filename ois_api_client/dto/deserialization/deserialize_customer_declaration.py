import xml.etree.ElementTree as ET
from typing import Union

from .XmlReader import XmlReader as XR
from ..CustomerDeclaration import CustomerDeclaration
from ..ProductStream import ProductStream
from ...constants import NAMESPACE_DATA


def deserialize_customer_declaration(element: ET.Element) -> Union[CustomerDeclaration, None]:
    if element is None:
        return None

    product_stream = XR.get_child_text(element, 'productStream', NAMESPACE_DATA)

    result = CustomerDeclaration(
        product_stream=ProductStream(product_stream) if product_stream is not None else None,
        product_fee_weight=XR.get_child_float(element, 'productFeeWeight', NAMESPACE_DATA)
    )

    return result
