from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import DATA
from ..dto.InvoiceMain import InvoiceMain
from .deserialize_batch_invoice import deserialize_batch_invoice
from .deserialize_invoice import deserialize_invoice


def deserialize_invoice_main(element: ET.Element) -> Optional[InvoiceMain]:
    if element is None:
        return None

    result = InvoiceMain(
        invoice=deserialize_invoice(
            XR.find_child(element, 'invoice', DATA)
        ),
        batch_invoice=[deserialize_batch_invoice(e) for e in XR.find_all_child(element, 'batchInvoice', DATA)],
    )

    return result
