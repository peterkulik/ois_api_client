import xml.etree.ElementTree as ET
from typing import Union

from .serialize_element import serialize_text_element, serialize_date_element, serialize_datetime_element, \
    serialize_date_interval, serialize_datetime_interval
from ..MandatoryQueryParams import MandatoryQueryParams as MQP


def _serialize_invoice_issue_date(parent: ET.Element, data: MQP.InvoiceIssueDate) -> ET.Element:
    return serialize_date_interval(parent, 'invoiceIssueDate', data.invoice_issue_date.date_from,
                                   data.invoice_issue_date.date_to)


def _serialize_original_invoice_number(parent: ET.Element,
                                       data: MQP.OriginalInvoiceNumber) -> ET.Element:
    return serialize_text_element(parent, 'originalInvoiceNumber', data.original_invoice_number)


def _serialize_ins_date(parent: ET.Element, data: MQP.InsDate) -> ET.Element:
    return serialize_datetime_interval(parent, 'insDate', data.ins_date.date_time_from, data.ins_date.datetime_to)


serializers = {MQP.InvoiceIssueDate: _serialize_invoice_issue_date,
               MQP.OriginalInvoiceNumber: _serialize_original_invoice_number,
               MQP.InsDate: _serialize_ins_date}


def serialize_mandatory_query_params(parent: ET.Element,
                                     data: Union[
                                         MQP.InvoiceIssueDate, MQP.OriginalInvoiceNumber, MQP.InsDate]) -> ET.Element:
    result = ET.SubElement(parent, 'mandatoryQueryParams')
    return serializers[type(data)](result, data)
