from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import DATA
from ..dto.PaymentEvidenceDocumentData import PaymentEvidenceDocumentData
from .deserialize_address import deserialize_address
from .deserialize_tax_number import deserialize_tax_number


def deserialize_payment_evidence_document_data(element: ET.Element) -> Optional[PaymentEvidenceDocumentData]:
    if element is None:
        return None

    result = PaymentEvidenceDocumentData(
        evidence_document_no=XR.get_child_text(element, 'evidenceDocumentNo', DATA),
        evidence_document_date=XR.get_child_date(element, 'evidenceDocumentDate', DATA),
        obligated_name=XR.get_child_text(element, 'obligatedName', DATA),
        obligated_address=deserialize_address(
            XR.find_child(element, 'obligatedAddress', DATA)
        ),
        obligated_tax_number=deserialize_tax_number(
            XR.find_child(element, 'obligatedTaxNumber', DATA)
        ),
    )

    return result
