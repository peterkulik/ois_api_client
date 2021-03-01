from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import BASE
from ..namespaces import COMMON
from ..namespaces import API
from ..dto.TokenExchangeResponse import TokenExchangeResponse
from .deserialize_basic_header import deserialize_basic_header
from .deserialize_basic_result import deserialize_basic_result
from .deserialize_software import deserialize_software


def deserialize_token_exchange_response(element: ET.Element) -> Optional[TokenExchangeResponse]:
    if element is None:
        return None

    result = TokenExchangeResponse(
        header=deserialize_basic_header(
            XR.find_child(element, 'header', COMMON)
        ),
        result=deserialize_basic_result(
            XR.find_child(element, 'result', COMMON)
        ),
        software=deserialize_software(
            XR.find_child(element, 'software', API)
        ),
        encoded_exchange_token=XR.get_child_text(element, 'encodedExchangeToken', API),
        token_validity_from=XR.get_child_datetime(element, 'tokenValidityFrom', API),
        token_validity_to=XR.get_child_datetime(element, 'tokenValidityTo', API),
    )

    return result
