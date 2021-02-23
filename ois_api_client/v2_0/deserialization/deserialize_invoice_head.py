from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import DATA
from ..dto.InvoiceHead import InvoiceHead
from .deserialize_customer_info import deserialize_customer_info
from .deserialize_fiscal_representative import deserialize_fiscal_representative
from .deserialize_invoice_detail import deserialize_invoice_detail
from .deserialize_supplier_info import deserialize_supplier_info


def deserialize_invoice_head(element: ET.Element) -> Optional[InvoiceHead]:
    if element is None:
        return None

    result = InvoiceHead(
        supplier_info=deserialize_supplier_info(
            XR.find_child(element, 'supplierInfo', DATA)
        ),
        customer_info=deserialize_customer_info(
            XR.find_child(element, 'customerInfo', DATA)
        ),
        fiscal_representative_info=deserialize_fiscal_representative(
            XR.find_child(element, 'fiscalRepresentativeInfo', DATA)
        ),
        invoice_detail=deserialize_invoice_detail(
            XR.find_child(element, 'invoiceDetail', DATA)
        ),
    )

    return result
