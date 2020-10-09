import xml.etree.ElementTree as ET

from .XmlReader import XmlReader as XR
from .deserialize_basic_result import deserialize_basic_result
from ..GeneralErrorResponse import GeneralErrorResponse
from ..TechnicalValidationResult import TechnicalValidationResult


def deserialize_general_error_response(general_error_response: str):
    root: ET.Element = ET.fromstring(general_error_response)

    if root is None:
        return None

    result = GeneralErrorResponse(result=deserialize_basic_result(root))

    tvm_list_el = XR.find_all_child(root, 'technicalValidationMessages')

    if tvm_list_el is None:
        return result

    for tvm_el in tvm_list_el:
        result.technical_validation_messages.append(
            TechnicalValidationResult(
                validation_result_code=XR.get_child_text(tvm_el, 'validationResultCode'),
                validation_error_code=XR.get_child_text(tvm_el, 'validationErrorCode'),
                message=XR.get_child_text(tvm_el, 'message')
            )
        )

    return result
