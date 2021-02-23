from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import COMMON
from ..namespaces import API
from ...deserialization.create_enum import create_enum
from ..dto.BusinessValidationResult import BusinessValidationResult
from ..dto.BusinessResultCode import BusinessResultCode
from .deserialize_pointer import deserialize_pointer


def deserialize_business_validation_result(element: ET.Element) -> Optional[BusinessValidationResult]:
    if element is None:
        return None

    result = BusinessValidationResult(
        validation_result_code=create_enum(BusinessResultCode, XR.get_child_text(element, 'validationResultCode', API)),
        validation_error_code=XR.get_child_text(element, 'validationErrorCode', API),
        message=XR.get_child_text(element, 'message', API),
        pointer=deserialize_pointer(
            XR.find_child(element, 'pointer', API)
        ),
    )

    return result
