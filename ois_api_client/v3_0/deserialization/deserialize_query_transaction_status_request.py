from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import COMMON
from ..namespaces import API
from ..dto.QueryTransactionStatusRequest import QueryTransactionStatusRequest
from .deserialize_basic_header import deserialize_basic_header
from .deserialize_software import deserialize_software
from .deserialize_user_header import deserialize_user_header


def deserialize_query_transaction_status_request(element: ET.Element) -> Optional[QueryTransactionStatusRequest]:
    if element is None:
        return None

    result = QueryTransactionStatusRequest(
        header=deserialize_basic_header(
            XR.find_child(element, 'header', COMMON)
        ),
        user=deserialize_user_header(
            XR.find_child(element, 'user', COMMON)
        ),
        software=deserialize_software(
            XR.find_child(element, 'software', API)
        ),
        transaction_id=XR.get_child_text(element, 'transactionId', API),
        return_original_request=XR.get_child_bool(element, 'returnOriginalRequest', API),
    )

    return result
