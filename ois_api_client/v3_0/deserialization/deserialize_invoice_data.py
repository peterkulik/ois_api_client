from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import BASE
from ..namespaces import DATA
from ..namespaces import COMMON
from ..dto.InvoiceData import InvoiceData
from .deserialize_invoice_main import deserialize_invoice_main


def deserialize_invoice_data(element: ET.Element) -> Optional[InvoiceData]:
    if element is None:
        return None

    result = InvoiceData(
        invoice_number=XR.get_child_text(element, 'invoiceNumber', DATA),
        invoice_issue_date=XR.get_child_date(element, 'invoiceIssueDate', DATA),
        completeness_indicator=XR.get_child_bool(element, 'completenessIndicator', DATA),
        invoice_main=deserialize_invoice_main(
            XR.find_child(element, 'invoiceMain', DATA)
        ),
    )

    return result
