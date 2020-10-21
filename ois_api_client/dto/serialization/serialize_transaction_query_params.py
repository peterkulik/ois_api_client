import xml.etree.ElementTree as ET
from typing import Union

from .serialize_element import serialize_text_element, serialize_int_element
from ..TransactionQueryParams import TransactionQueryParams


def serialize_transaction_query_params(parent: ET.Element, params: TransactionQueryParams) -> Union[ET.Element, None]:
    if params is None:
        return None

    result = ET.SubElement(parent, 'transactionQueryParams')

    serialize_text_element(result, 'transactionId', params.transaction_id)
    serialize_int_element(result, 'index', params.index)

    if params.invoice_operation is not None:
        serialize_text_element(result, 'invoiceOperation', params.invoice_operation.value)

    return result
