from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import COMMON
from ..namespaces import API
from ..dto.QueryTransactionStatusResponse import QueryTransactionStatusResponse
from .deserialize_basic_header import deserialize_basic_header
from .deserialize_basic_result import deserialize_basic_result
from .deserialize_processing_result_list import deserialize_processing_result_list
from .deserialize_software import deserialize_software


def deserialize_query_transaction_status_response(element: ET.Element) -> Optional[QueryTransactionStatusResponse]:
    if element is None:
        return None

    result = QueryTransactionStatusResponse(
        header=deserialize_basic_header(
            XR.find_child(element, 'header', COMMON)
        ),
        result=deserialize_basic_result(
            XR.find_child(element, 'result', COMMON)
        ),
        software=deserialize_software(
            XR.find_child(element, 'software', API)
        ),
        processing_results=deserialize_processing_result_list(
            XR.find_child(element, 'processingResults', API)
        ),
    )

    return result
