import xml.etree.ElementTree as ET
from typing import Union

from .XmlReader import XmlReader as XR
from .deserialize_basic_result import deserialize_basic_result
from ..AuditData import AuditData
from ..InvoiceDataResult import InvoiceDataResult
from ..OriginalRequestVersion import OriginalRequestVersion
from ..QueryInvoiceDataResponse import QueryInvoiceDataResponse
from ..Source import Source


def _deserialize_audit_data(parent: ET.Element) -> Union[AuditData, None]:
    audit_el = XR.find_child(parent, 'auditData')

    if audit_el is None:
        return None

    result = AuditData(
        ins_date=XR.get_child_utc_datetime(audit_el, 'insdate'),
        ins_cus_user=XR.get_child_text(audit_el, 'insCusUser'),
        source=Source(XR.get_child_text(audit_el, 'source')),
        transaction_id=XR.get_child_text(audit_el, 'transactionId'),
        index=XR.get_child_int(audit_el, 'index'),
        batch_index=XR.get_child_int(audit_el, 'batchIndex'),
        original_request_version=OriginalRequestVersion(XR.get_child_text(audit_el, 'originalRequestVersion'))
    )

    return result


def _deserialize_invoice_data_result(parent: ET.Element) -> Union[InvoiceDataResult, None]:
    if parent is None:
        return None

    result = InvoiceDataResult(
        invoice_data=XR.get_child_text(parent, 'invoiceData'),
        audit_data=_deserialize_audit_data(parent),
        compressed_content_indicator=XR.get_child_bool(parent, 'compressedContentIndicator')
    )

    return result


def deserialize_query_invoice_data_response(query_invoice_data_response: str) -> QueryInvoiceDataResponse:
    root: ET.Element = ET.fromstring(query_invoice_data_response)

    if root is None:
        raise ValueError('query_invoice_data_response is not a valid xml')

    idr_el = XR.find_child(root, 'invoiceDataResult')

    result = QueryInvoiceDataResponse(
        result=deserialize_basic_result(root),
        invoice_data_result=_deserialize_invoice_data_result(idr_el)
    )
    return result
