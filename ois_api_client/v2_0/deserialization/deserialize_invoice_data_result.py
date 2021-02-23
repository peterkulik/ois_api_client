from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import API
from ..dto.InvoiceDataResult import InvoiceDataResult
from .deserialize_audit_data import deserialize_audit_data


def deserialize_invoice_data_result(element: ET.Element) -> Optional[InvoiceDataResult]:
    if element is None:
        return None

    result = InvoiceDataResult(
        invoice_data=XR.get_child_text(element, 'invoiceData', API),
        audit_data=deserialize_audit_data(
            XR.find_child(element, 'auditData', API)
        ),
        compressed_content_indicator=XR.get_child_bool(element, 'compressedContentIndicator', API),
    )

    return result
