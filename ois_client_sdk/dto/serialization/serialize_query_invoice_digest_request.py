import xml.etree.ElementTree as ET

from ..QueryInvoiceDigestRequest import QueryInvoiceDigestRequest
from .serialize_basic import serialize_basic
from .serialize_text_element import serialize_text_element, serialize_int_element


def serialize_query_invoice_digest_request(data: QueryInvoiceDigestRequest, request_signature: str,
                                           password_hash: str) -> ET.Element:
    root = serialize_basic(data, 'QueryInvoiceDigestRequest', request_signature, password_hash)

    serialize_int_element(root, 'page', data.page)
    serialize_text_element(root, 'invoiceDirection', data.invoice_direction.value)


    return root
