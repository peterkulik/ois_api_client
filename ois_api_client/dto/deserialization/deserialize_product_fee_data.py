import xml.etree.ElementTree as ET
from typing import Union

from .XmlReader import XmlReader as XR
from .deserialize_product_code import deserialize_product_code
from ..ProductFeeData import ProductFeeData
from ..ProductFeeMeasuringUnit import ProductFeeMeasuringUnit
from ...constants import NAMESPACE_DATA


def deserialize_product_fee_data(element: ET.Element) -> Union[ProductFeeData, None]:
    if element is None:
        return None

    product_fee_measuring_unit = XR.find_child(element, 'productFeeMeasuringUnit', NAMESPACE_DATA)

    result = ProductFeeData(
        product_fee_code=deserialize_product_code(XR.find_child(element, 'productFeeCode', NAMESPACE_DATA)),
        product_fee_quantity=XR.get_child_float(element, 'productFeeQuantity', NAMESPACE_DATA),
        product_fee_measuring_unit=ProductFeeMeasuringUnit(
            product_fee_measuring_unit) if product_fee_measuring_unit is not None else None,
        product_fee_rate=XR.get_child_float(element, 'productFeeRate', NAMESPACE_DATA),
        product_fee_amount=XR.get_child_float(element, 'productFeeAmount', NAMESPACE_DATA)
    )

    return result
