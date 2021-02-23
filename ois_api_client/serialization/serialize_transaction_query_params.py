import xml.etree.ElementTree as ET
from typing import Optional

from .serialize_element import serialize_text_element, serialize_int_element
from ..v3_0 import dto, namespaces as ns


def serialize_transaction_query_params(parent: ET.Element, params: dto.TransactionQueryParams) -> Optional[ET.Element]:
    if params is None:
        return None

    result = ET.SubElement(parent, 'transactionQueryParams')

    serialize_text_element(result, 'transactionId', params.transaction_id, ns.API)
    serialize_int_element(result, 'index', params.index, ns.API)

    if params.invoice_operation is not None:
        serialize_text_element(result, 'invoiceOperation', params.invoice_operation.value, ns.API)

    return result
