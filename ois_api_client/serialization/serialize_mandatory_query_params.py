import xml.etree.ElementTree as ET
from .serialize_element import serialize_text_element, serialize_date_interval, serialize_datetime_interval
from ..v3_0 import dto, namespaces as ns


def serialize_mandatory_query_params(parent: ET.Element,
                                     mandatory_query_params: dto.MandatoryQueryParams) -> ET.Element:
    result = ET.SubElement(parent, 'mandatoryQueryParams')

    if mandatory_query_params.invoice_issue_date:
        return serialize_date_interval(result,
                                       'invoiceIssueDate',
                                       mandatory_query_params.invoice_issue_date.date_from,
                                       mandatory_query_params.invoice_issue_date.date_to)

    if mandatory_query_params.original_invoice_number:
        return serialize_text_element(result,
                                      'originalInvoiceNumber',
                                      mandatory_query_params.original_invoice_number,
                                      ns.API)

    if mandatory_query_params.ins_date:
        return serialize_datetime_interval(result,
                                           'insDate',
                                           mandatory_query_params.ins_date.date_time_from,
                                           mandatory_query_params.ins_date.date_time_to)
