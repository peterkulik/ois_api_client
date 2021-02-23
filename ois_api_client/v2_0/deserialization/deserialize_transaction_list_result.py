from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import API
from ..dto.TransactionListResult import TransactionListResult
from .deserialize_transaction import deserialize_transaction


def deserialize_transaction_list_result(element: ET.Element) -> Optional[TransactionListResult]:
    if element is None:
        return None

    result = TransactionListResult(
        current_page=XR.get_child_int(element, 'currentPage', API),
        available_page=XR.get_child_int(element, 'availablePage', API),
        transaction=[deserialize_transaction(e) for e in XR.find_all_child(element, 'transaction', API)],
    )

    return result
