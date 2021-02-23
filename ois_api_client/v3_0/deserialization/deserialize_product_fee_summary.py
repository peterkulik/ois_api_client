from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import BASE
from ..namespaces import DATA
from ...deserialization.create_enum import create_enum
from ..dto.ProductFeeSummary import ProductFeeSummary
from ..dto.ProductFeeOperation import ProductFeeOperation
from .deserialize_payment_evidence_document_data import deserialize_payment_evidence_document_data
from .deserialize_product_fee_data import deserialize_product_fee_data


def deserialize_product_fee_summary(element: ET.Element) -> Optional[ProductFeeSummary]:
    if element is None:
        return None

    result = ProductFeeSummary(
        product_fee_operation=create_enum(ProductFeeOperation, XR.get_child_text(element, 'productFeeOperation', DATA)),
        product_fee_data=[deserialize_product_fee_data(e) for e in XR.find_all_child(element, 'productFeeData', DATA)],
        product_charge_sum=XR.get_child_float(element, 'productChargeSum', DATA),
        payment_evidence_document_data=deserialize_payment_evidence_document_data(
            XR.find_child(element, 'paymentEvidenceDocumentData', DATA)
        ),
    )

    return result
