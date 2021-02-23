from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import API
from ..namespaces import DATA
from ...deserialization.create_enum import create_enum
from ..dto.Transaction import Transaction
from ..dto.Source import Source
from ..dto.OriginalRequestVersion import OriginalRequestVersion


def deserialize_transaction(element: ET.Element) -> Optional[Transaction]:
    if element is None:
        return None

    result = Transaction(
        ins_date=XR.get_child_datetime(element, 'insDate', API),
        ins_cus_user=XR.get_child_text(element, 'insCusUser', API),
        source=create_enum(Source, XR.get_child_text(element, 'source', API)),
        transaction_id=XR.get_child_text(element, 'transactionId', API),
        original_request_version=create_enum(OriginalRequestVersion, XR.get_child_text(element, 'originalRequestVersion', API)),
        item_count=XR.get_child_int(element, 'itemCount', API),
    )

    return result
