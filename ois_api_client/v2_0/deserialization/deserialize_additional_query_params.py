from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import API
from ..namespaces import DATA
from ...deserialization.create_enum import create_enum
from ..dto.AdditionalQueryParams import AdditionalQueryParams
from ..dto.InvoiceCategory import InvoiceCategory
from ..dto.PaymentMethod import PaymentMethod
from ..dto.InvoiceAppearance import InvoiceAppearance
from ..dto.Source import Source


def deserialize_additional_query_params(element: ET.Element) -> Optional[AdditionalQueryParams]:
    if element is None:
        return None

    result = AdditionalQueryParams(
        tax_number=XR.get_child_text(element, 'taxNumber', API),
        group_member_tax_number=XR.get_child_text(element, 'groupMemberTaxNumber', API),
        name=XR.get_child_text(element, 'name', API),
        invoice_category=create_enum(InvoiceCategory, XR.get_child_text(element, 'invoiceCategory', API)),
        payment_method=create_enum(PaymentMethod, XR.get_child_text(element, 'paymentMethod', API)),
        invoice_appearance=create_enum(InvoiceAppearance, XR.get_child_text(element, 'invoiceAppearance', API)),
        source=create_enum(Source, XR.get_child_text(element, 'source', API)),
        currency=XR.get_child_text(element, 'currency', API),
    )

    return result
