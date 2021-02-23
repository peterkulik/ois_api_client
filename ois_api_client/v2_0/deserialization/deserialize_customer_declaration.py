from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import DATA
from ...deserialization.create_enum import create_enum
from ..dto.CustomerDeclaration import CustomerDeclaration
from ..dto.ProductStream import ProductStream


def deserialize_customer_declaration(element: ET.Element) -> Optional[CustomerDeclaration]:
    if element is None:
        return None

    result = CustomerDeclaration(
        product_stream=create_enum(ProductStream, XR.get_child_text(element, 'productStream', DATA)),
        product_fee_weight=XR.get_child_float(element, 'productFeeWeight', DATA),
    )

    return result
