import xml.etree.ElementTree as ET
from typing import Optional

from .XmlReader import XmlReader as XR
from .deserialize_invoice import deserialize_invoice
from ..BatchInvoice import BatchInvoice
from ...constants import NAMESPACE_DATA


def deserialize_batch_invoice(element: ET.Element) -> Optional[BatchInvoice]:
    if element is None:
        return None

    result = BatchInvoice(
        batch_index=XR.get_child_int(element, 'batchIndex', NAMESPACE_DATA),
        invoice=deserialize_invoice(XR.find_child(element, 'invoice', NAMESPACE_DATA))
    )

    return result
