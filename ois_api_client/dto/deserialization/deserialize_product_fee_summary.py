import xml.etree.ElementTree as ET
from typing import Union

from .XmlReader import XmlReader as XR
from .deserialize_payment_evidence_document_data import deserialize_payment_evidence_document_data
from .deserialize_product_fee_data import deserialize_product_fee_data
from ..ProductFeeOperation import ProductFeeOperation
from ..ProductFeeSummary import ProductFeeSummary
from ...constants import NAMESPACE_DATA


def deserialize_product_fee_summary(element: ET.Element) -> Union[ProductFeeSummary, None]:
    if element is None:
        return None

    product_fee_operation = XR.get_child_text(element, 'productFeeOperation', NAMESPACE_DATA)

    result = ProductFeeSummary(
        product_fee_operation=ProductFeeOperation(product_fee_operation) if product_fee_operation is not None else None,
        product_fee_data=[deserialize_product_fee_data(el) for el in
                          XR.find_all_child(element, 'productFeeData', NAMESPACE_DATA)],
        product_charge_sum=XR.get_child_float(element, 'productChargeSum', NAMESPACE_DATA),
        payment_evidence_document_data=deserialize_payment_evidence_document_data(
            XR.find_child(element, 'paymentEvidenceDocumentData', NAMESPACE_DATA)
        )
    )

    return result
