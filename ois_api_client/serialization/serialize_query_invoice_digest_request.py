import xml.etree.ElementTree as ET

from .serialize_additional_query_params import serialize_additional_query_params
from .serialize_basic_online_invoice_request import serialize_basic_online_invoice_request
from .serialize_element import serialize_text_element, serialize_int_element
from .serialize_mandatory_query_params import serialize_mandatory_query_params
from .serialize_relational_query_params import serialize_relational_query_params
from .serialize_transaction_query_params import serialize_transaction_query_params
from ..v3_0 import dto, namespaces as ns


def serialize_query_invoice_digest_request(data: dto.QueryInvoiceDigestRequest) -> ET.Element:
    root = serialize_basic_online_invoice_request(data, 'QueryInvoiceDigestRequest')

    serialize_int_element(root, 'page', data.page, ns.API)
    serialize_text_element(root, 'invoiceDirection', data.invoice_direction.value, ns.API)

    query_params_element = ET.SubElement(root, 'invoiceQueryParams')
    serialize_mandatory_query_params(query_params_element, data.invoice_query_params.mandatory_query_params)
    serialize_additional_query_params(query_params_element, data.invoice_query_params.additional_query_params)
    serialize_relational_query_params(query_params_element, data.invoice_query_params.relational_query_params)
    serialize_transaction_query_params(query_params_element, data.invoice_query_params.transaction_query_params)
    return root
