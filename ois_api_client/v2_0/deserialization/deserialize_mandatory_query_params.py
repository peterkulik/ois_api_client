from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import API
from ..namespaces import DATA
from ..dto.MandatoryQueryParams import MandatoryQueryParams
from .deserialize_date_interval_param import deserialize_date_interval_param
from .deserialize_date_time_interval_param import deserialize_date_time_interval_param


def deserialize_mandatory_query_params(element: ET.Element) -> Optional[MandatoryQueryParams]:
    if element is None:
        return None

    result = MandatoryQueryParams(
        invoice_issue_date=deserialize_date_interval_param(
            XR.find_child(element, 'invoiceIssueDate', API)
        ),
        ins_date=deserialize_date_time_interval_param(
            XR.find_child(element, 'insDate', API)
        ),
        original_invoice_number=XR.get_child_text(element, 'originalInvoiceNumber', API),
    )

    return result
