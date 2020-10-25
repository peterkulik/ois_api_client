import xml.etree.ElementTree as ET
from typing import Union

from .XmlReader import XmlReader as XR
from .deserialize_address import deserialize_address
from .deserialize_tax_number import deserialize_tax_number
from ..PaymentEvidenceDocumentData import PaymentEvidenceDocumentData
from ...constants import NAMESPACE_DATA


def deserialize_payment_evidence_document_data(element: ET.Element) -> Union[PaymentEvidenceDocumentData, None]:
    if element is None:
        return None

    result = PaymentEvidenceDocumentData(
        evidence_document_no=XR.get_child_text(element, 'evidenceDocumentNo', NAMESPACE_DATA),
        evidence_document_date=XR.get_child_date(element, 'evidenceDocumentDate', NAMESPACE_DATA),
        obligated_name=XR.get_child_text(element, 'obligatedName', NAMESPACE_DATA),
        obligated_address=deserialize_address(XR.find_child(element, 'obligatedAddress', NAMESPACE_DATA)),
        obligated_tax_number=deserialize_tax_number(XR.find_child(element, 'obligatedTaxNumber', NAMESPACE_DATA))
    )

    return result

