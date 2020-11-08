import xml.etree.ElementTree as ET

from .XmlReader import XmlReader as XR
from .deserialize_basic_header import deserialize_basic_header
from .deserialize_basic_result import deserialize_basic_result
from .deserialize_software import deserialize_software
from ..GeneralErrorResponse import GeneralErrorResponse
from ..TechnicalValidationResult import TechnicalValidationResult
from ...constants import NAMESPACE_COMMON, NAMESPACE_API


def deserialize_general_error_response(general_error_response: str):
    root: ET.Element = ET.fromstring(general_error_response)

    if root is None:
        return None

    result = GeneralErrorResponse(
        header=deserialize_basic_header(root),
        result=deserialize_basic_result(root),
        software=deserialize_software(root)
    )

    tvm_list_el = XR.find_all_child(root, 'technicalValidationMessages', NAMESPACE_API)

    if tvm_list_el is None:
        return result

    for tvm_el in tvm_list_el:
        result.technical_validation_messages.append(
            TechnicalValidationResult(
                validation_result_code=XR.get_child_text(tvm_el, 'validationResultCode', NAMESPACE_COMMON),
                validation_error_code=XR.get_child_text(tvm_el, 'validationErrorCode', NAMESPACE_COMMON),
                message=XR.get_child_text(tvm_el, 'message', NAMESPACE_COMMON)
            )
        )

    return result
