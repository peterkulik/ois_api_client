from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import API
from ..dto.QueryTransactionListRequest import QueryTransactionListRequest
from .deserialize_basic_header import deserialize_basic_header
from .deserialize_date_time_interval_param import deserialize_date_time_interval_param
from .deserialize_software import deserialize_software
from .deserialize_user_header import deserialize_user_header


def deserialize_query_transaction_list_request(element: ET.Element) -> Optional[QueryTransactionListRequest]:
    if element is None:
        return None

    result = QueryTransactionListRequest(
        header=deserialize_basic_header(
            XR.find_child(element, 'header', API)
        ),
        user=deserialize_user_header(
            XR.find_child(element, 'user', API)
        ),
        software=deserialize_software(
            XR.find_child(element, 'software', API)
        ),
        page=XR.get_child_int(element, 'page', API),
        ins_date=deserialize_date_time_interval_param(
            XR.find_child(element, 'insDate', API)
        ),
    )

    return result
