from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import BASE
from ..namespaces import DATA
from ..dto.BatchInvoice import BatchInvoice
from .deserialize_invoice import deserialize_invoice


def deserialize_batch_invoice(element: ET.Element) -> Optional[BatchInvoice]:
    if element is None:
        return None

    result = BatchInvoice(
        batch_index=XR.get_child_int(element, 'batchIndex', DATA),
        invoice=deserialize_invoice(
            XR.find_child(element, 'invoice', DATA)
        ),
    )

    return result
