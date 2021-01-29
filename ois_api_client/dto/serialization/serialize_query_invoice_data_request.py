import xml.etree.ElementTree as ET

from .serialize_basic_online_invoice_request import serialize_basic_online_invoice_request
from .serialize_element import serialize_text_element, serialize_int_element
from .. import QueryInvoiceDataRequest
from ... import NAMESPACE_API


def serialize_query_invoice_data_request_type(parent: ET.Element, data: QueryInvoiceDataRequest) -> ET.Element:
    result = ET.SubElement(parent, 'invoiceNumberQuery')

    serialize_text_element(result, 'invoiceNumber', data.invoice_number_query.invoice_number, NAMESPACE_API
                           )
    serialize_text_element(result, 'invoiceDirection', data.invoice_number_query.invoice_direction.value,
                           NAMESPACE_API)

    if data.invoice_number_query.batch_index is not None:
        serialize_int_element(result, 'batchIndex', data.invoice_number_query.batch_index, NAMESPACE_API)

    if data.invoice_number_query.supplier_tax_number is not None:
        serialize_text_element(result, 'supplierTaxNumber', data.invoice_number_query.supplier_tax_number,
                               NAMESPACE_API)

    return result


def serialize_query_invoice_data_request(data: QueryInvoiceDataRequest, request_signature: str,
                                         password_hash: str) -> ET.Element:
    root = serialize_basic_online_invoice_request(data, 'QueryInvoiceDataRequest', request_signature, password_hash)
    serialize_query_invoice_data_request_type(root, data)
    return root
