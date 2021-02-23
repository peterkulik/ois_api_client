from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import COMMON
from ..namespaces import API
from ..dto.QueryTransactionListResponse import QueryTransactionListResponse
from .deserialize_basic_header import deserialize_basic_header
from .deserialize_basic_result import deserialize_basic_result
from .deserialize_software import deserialize_software
from .deserialize_transaction_list_result import deserialize_transaction_list_result


def deserialize_query_transaction_list_response(element: ET.Element) -> Optional[QueryTransactionListResponse]:
    if element is None:
        return None

    result = QueryTransactionListResponse(
        header=deserialize_basic_header(
            XR.find_child(element, 'header', COMMON)
        ),
        result=deserialize_basic_result(
            XR.find_child(element, 'result', COMMON)
        ),
        software=deserialize_software(
            XR.find_child(element, 'software', API)
        ),
        transaction_list_result=deserialize_transaction_list_result(
            XR.find_child(element, 'transactionListResult', API)
        ),
    )

    return result
