from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import API
from ..namespaces import DATA
from ...deserialization.create_enum import create_enum
from ..dto.TransactionQueryParams import TransactionQueryParams
from ..dto.ManageInvoiceOperation import ManageInvoiceOperation


def deserialize_transaction_query_params(element: ET.Element) -> Optional[TransactionQueryParams]:
    if element is None:
        return None

    result = TransactionQueryParams(
        transaction_id=XR.get_child_text(element, 'transactionId', API),
        index=XR.get_child_int(element, 'index', API),
        invoice_operation=create_enum(ManageInvoiceOperation, XR.get_child_text(element, 'invoiceOperation', API)),
    )

    return result
