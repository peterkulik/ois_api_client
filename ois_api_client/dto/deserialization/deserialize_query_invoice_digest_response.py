import xml.etree.ElementTree as ET

from .deserialize_basic_header import deserialize_basic_header
from .deserialize_basic_result import deserialize_basic_result
from .deserialize_invoice_digest_result import deserialize_invoice_digest_result
from .deserialize_software import deserialize_software
from ..QueryInvoiceDigestResponse import QueryInvoiceDigestResponse


def deserialize_query_invoice_digest_response(query_invoice_digest_response: str) -> QueryInvoiceDigestResponse:
    root: ET.Element = ET.fromstring(query_invoice_digest_response)

    if root is None:
        raise ValueError('query_invoice_digest_response is not a valid xml')

    result = QueryInvoiceDigestResponse(
        header=deserialize_basic_header(root),
        result=deserialize_basic_result(root),
        software=deserialize_software(root),
        invoice_digest_result=deserialize_invoice_digest_result(root)
    )
    return result
