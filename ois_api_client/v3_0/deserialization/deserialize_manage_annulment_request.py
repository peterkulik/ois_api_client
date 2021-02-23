from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import COMMON
from ..namespaces import API
from ..dto.ManageAnnulmentRequest import ManageAnnulmentRequest
from .deserialize_annulment_operation_list import deserialize_annulment_operation_list
from .deserialize_basic_header import deserialize_basic_header
from .deserialize_software import deserialize_software
from .deserialize_user_header import deserialize_user_header


def deserialize_manage_annulment_request(element: ET.Element) -> Optional[ManageAnnulmentRequest]:
    if element is None:
        return None

    result = ManageAnnulmentRequest(
        header=deserialize_basic_header(
            XR.find_child(element, 'header', COMMON)
        ),
        user=deserialize_user_header(
            XR.find_child(element, 'user', COMMON)
        ),
        software=deserialize_software(
            XR.find_child(element, 'software', API)
        ),
        exchange_token=XR.get_child_text(element, 'exchangeToken', API),
        annulment_operations=deserialize_annulment_operation_list(
            XR.find_child(element, 'annulmentOperations', API)
        ),
    )

    return result
