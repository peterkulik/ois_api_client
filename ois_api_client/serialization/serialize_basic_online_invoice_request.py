import xml.etree.ElementTree as ET

from .serialize_header import serialize_header
from .serialize_user import serialize_user
from .serialize_software import serialize_software
from ..v3_0 import dto, namespaces as ns
from ..xml.get_full_tag import get_full_tag


def serialize_basic_online_invoice_request(data: dto.BasicOnlineInvoiceRequest,
                                           root_element: str) -> ET.Element:
    root = ET.Element(get_full_tag(ns.API, root_element))
    root.append(serialize_header(data.header))
    root.append(serialize_user(data.user))
    root.append(serialize_software(data.software))

    return root
