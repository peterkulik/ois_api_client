from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import DATA
from ...deserialization.create_enum import create_enum
from ..dto.ProductFeeData import ProductFeeData
from ..dto.ProductFeeMeasuringUnit import ProductFeeMeasuringUnit
from .deserialize_product_code import deserialize_product_code


def deserialize_product_fee_data(element: ET.Element) -> Optional[ProductFeeData]:
    if element is None:
        return None

    result = ProductFeeData(
        product_fee_code=deserialize_product_code(
            XR.find_child(element, 'productFeeCode', DATA)
        ),
        product_fee_quantity=XR.get_child_float(element, 'productFeeQuantity', DATA),
        product_fee_measuring_unit=create_enum(ProductFeeMeasuringUnit, XR.get_child_text(element, 'productFeeMeasuringUnit', DATA)),
        product_fee_rate=XR.get_child_float(element, 'productFeeRate', DATA),
        product_fee_amount=XR.get_child_float(element, 'productFeeAmount', DATA),
    )

    return result
