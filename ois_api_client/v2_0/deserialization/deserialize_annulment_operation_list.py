from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import API
from ..dto.AnnulmentOperationList import AnnulmentOperationList
from .deserialize_annulment_operation import deserialize_annulment_operation


def deserialize_annulment_operation_list(element: ET.Element) -> Optional[AnnulmentOperationList]:
    if element is None:
        return None

    result = AnnulmentOperationList(
        annulment_operation=[deserialize_annulment_operation(e) for e in XR.find_all_child(element, 'annulmentOperation', API)],
    )

    return result
