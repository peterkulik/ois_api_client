import xml.etree.ElementTree as ET
from typing import Union

from .XmlReader import XmlReader as XR
from .deserialize_invoice_head import deserialize_invoice_head
from .deserialize_invoice_lines import deserialize_invoice_lines
from .deserialize_invoice_reference import deserialize_invoice_reference
from .deserialize_invoice_summary import deserialize_invoice_summary
from .deserialize_product_fee_summary import deserialize_product_fee_summary
from ..Invoice import Invoice
from ...constants import NAMESPACE_DATA


def deserialize_invoice(element: ET.Element) -> Union[Invoice, None]:
    if element is None:
        return None

    invoice_reference_el = XR.find_child(element, 'invoiceReference', NAMESPACE_DATA)
    invoice_head_el = XR.find_child(element, 'invoiceHead', NAMESPACE_DATA)
    invoice_lines_el = XR.find_child(element, 'invoiceLines', NAMESPACE_DATA)
    product_fee_summary_el = XR.find_child(element, 'productFeeSummary', NAMESPACE_DATA)
    invoice_summary_el = XR.find_child(element, 'invoiceSummary', NAMESPACE_DATA)

    result = Invoice(
        invoice_head=deserialize_invoice_head(invoice_head_el),
        invoice_summary=deserialize_invoice_summary(invoice_summary_el),
        invoice_reference=deserialize_invoice_reference(invoice_reference_el),
        invoice_lines=deserialize_invoice_lines(invoice_lines_el),
        product_fee_summary=deserialize_product_fee_summary(product_fee_summary_el)
    )

    return result
