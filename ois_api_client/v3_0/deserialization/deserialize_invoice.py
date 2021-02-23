from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import DATA
from ..dto.Invoice import Invoice
from .deserialize_invoice_head import deserialize_invoice_head
from .deserialize_invoice_reference import deserialize_invoice_reference
from .deserialize_lines import deserialize_lines
from .deserialize_product_fee_summary import deserialize_product_fee_summary
from .deserialize_summary import deserialize_summary


def deserialize_invoice(element: ET.Element) -> Optional[Invoice]:
    if element is None:
        return None

    result = Invoice(
        invoice_reference=deserialize_invoice_reference(
            XR.find_child(element, 'invoiceReference', DATA)
        ),
        invoice_head=deserialize_invoice_head(
            XR.find_child(element, 'invoiceHead', DATA)
        ),
        invoice_lines=deserialize_lines(
            XR.find_child(element, 'invoiceLines', DATA)
        ),
        product_fee_summary=[deserialize_product_fee_summary(e) for e in XR.find_all_child(element, 'productFeeSummary', DATA)],
        invoice_summary=deserialize_summary(
            XR.find_child(element, 'invoiceSummary', DATA)
        ),
    )

    return result
