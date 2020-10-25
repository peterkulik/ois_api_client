import xml.etree.ElementTree as ET
from typing import Union

from .XmlReader import XmlReader as XR
from .deserialize_customer_info import deserialize_customer_info
from .deserialize_fiscal_representative_info import deserialize_fiscal_representative_info
from .deserialize_invoice_detail import deserialize_invoice_detail
from .deserialize_supplier_info import deserialize_supplier_info
from ..InvoiceHead import InvoiceHead
from ...constants import NAMESPACE_DATA


def deserialize_invoice_head(element: ET.Element) -> Union[InvoiceHead, None]:
    if element is None:
        return None

    result = InvoiceHead(
        supplier_info=deserialize_supplier_info(XR.find_child(element, 'supplierInfo', NAMESPACE_DATA)),
        invoice_detail=deserialize_invoice_detail(XR.find_child(element, 'invoiceDetail', NAMESPACE_DATA)),
        customer_info=deserialize_customer_info(XR.find_child(element, 'customerInfo', NAMESPACE_DATA)),
        fiscal_representative_info=deserialize_fiscal_representative_info(
            XR.find_child(element, 'fiscalRepresentativeInfo', NAMESPACE_DATA))
    )

    return result
