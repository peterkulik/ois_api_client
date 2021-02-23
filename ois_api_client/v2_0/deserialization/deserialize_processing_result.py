from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import API
from ..namespaces import DATA
from ...deserialization.create_enum import create_enum
from ..dto.ProcessingResult import ProcessingResult
from ..dto.InvoiceStatus import InvoiceStatus
from .deserialize_business_validation_result import deserialize_business_validation_result
from .deserialize_technical_validation_result import deserialize_technical_validation_result


def deserialize_processing_result(element: ET.Element) -> Optional[ProcessingResult]:
    if element is None:
        return None

    result = ProcessingResult(
        index=XR.get_child_int(element, 'index', API),
        batch_index=XR.get_child_int(element, 'batchIndex', API),
        invoice_status=create_enum(InvoiceStatus, XR.get_child_text(element, 'invoiceStatus', API)),
        technical_validation_messages=[deserialize_technical_validation_result(e) for e in XR.find_all_child(element, 'technicalValidationMessages', API)],
        business_validation_messages=[deserialize_business_validation_result(e) for e in XR.find_all_child(element, 'businessValidationMessages', API)],
        compressed_content_indicator=XR.get_child_bool(element, 'compressedContentIndicator', API),
        original_request=XR.get_child_text(element, 'originalRequest', API),
    )

    return result
