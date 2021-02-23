from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import API
from ..namespaces import DATA
from ...deserialization.create_enum import create_enum
from ..dto.InvoiceChainDigest import InvoiceChainDigest
from ..dto.ManageInvoiceOperation import ManageInvoiceOperation
from ..dto.OriginalRequestVersion import OriginalRequestVersion


def deserialize_invoice_chain_digest(element: ET.Element) -> Optional[InvoiceChainDigest]:
    if element is None:
        return None

    result = InvoiceChainDigest(
        invoice_number=XR.get_child_text(element, 'invoiceNumber', API),
        batch_index=XR.get_child_int(element, 'batchIndex', API),
        invoice_operation=create_enum(ManageInvoiceOperation, XR.get_child_text(element, 'invoiceOperation', API)),
        supplier_tax_number=XR.get_child_text(element, 'supplierTaxNumber', API),
        customer_tax_number=XR.get_child_text(element, 'customerTaxNumber', API),
        ins_date=XR.get_child_datetime(element, 'insDate', API),
        original_request_version=create_enum(OriginalRequestVersion, XR.get_child_text(element, 'originalRequestVersion', API)),
    )

    return result
