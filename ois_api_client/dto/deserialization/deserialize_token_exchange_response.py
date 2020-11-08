import xml.etree.ElementTree as ET

from .XmlReader import XmlReader as XR
from .deserialize_basic_header import deserialize_basic_header
from .deserialize_basic_result import deserialize_basic_result
from .deserialize_software import deserialize_software
from ..TokenExchangeResponse import TokenExchangeResponse


def deserialize_token_exchange_response(token_exchange_response: str) -> TokenExchangeResponse:
    root: ET.Element = ET.fromstring(token_exchange_response)

    if root is None:
        raise ValueError('token_exchange_response is not a valid xml')

    result = TokenExchangeResponse(
        header=deserialize_basic_header(root),
        result=deserialize_basic_result(root),
        software=deserialize_software(root),
        encoded_exchange_token=XR.find_child(root, 'encodedExchangeToken').text,
        token_validity_from=XR.get_child_datetime_tz_offset(root, 'tokenValidityFrom'),
        token_validity_to=XR.get_child_datetime_tz_offset(root, 'tokenValidityTo')
    )
    return result
