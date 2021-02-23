from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import COMMON
from ..namespaces import API
from ..dto.QueryTaxpayerResponse import QueryTaxpayerResponse
from .deserialize_basic_header import deserialize_basic_header
from .deserialize_basic_result import deserialize_basic_result
from .deserialize_software import deserialize_software
from .deserialize_taxpayer_data import deserialize_taxpayer_data


def deserialize_query_taxpayer_response(element: ET.Element) -> Optional[QueryTaxpayerResponse]:
    if element is None:
        return None

    result = QueryTaxpayerResponse(
        header=deserialize_basic_header(
            XR.find_child(element, 'header', COMMON)
        ),
        result=deserialize_basic_result(
            XR.find_child(element, 'result', COMMON)
        ),
        software=deserialize_software(
            XR.find_child(element, 'software', API)
        ),
        info_date=XR.get_child_datetime(element, 'infoDate', API),
        taxpayer_validity=XR.get_child_bool(element, 'taxpayerValidity', API),
        taxpayer_data=deserialize_taxpayer_data(
            XR.find_child(element, 'taxpayerData', API)
        ),
    )

    return result
