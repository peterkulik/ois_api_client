from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import COMMON
from ...deserialization.create_enum import create_enum
from ..dto.TechnicalValidationResult import TechnicalValidationResult
from ..dto.TechnicalResultCode import TechnicalResultCode


def deserialize_technical_validation_result(element: ET.Element) -> Optional[TechnicalValidationResult]:
    if element is None:
        return None

    result = TechnicalValidationResult(
        validation_result_code=create_enum(TechnicalResultCode, XR.get_child_text(element, 'validationResultCode', COMMON)),
        validation_error_code=XR.get_child_text(element, 'validationErrorCode', COMMON),
        message=XR.get_child_text(element, 'message', COMMON),
    )

    return result
