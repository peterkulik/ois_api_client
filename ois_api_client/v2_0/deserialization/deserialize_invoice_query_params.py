from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import API
from ..dto.InvoiceQueryParams import InvoiceQueryParams
from .deserialize_additional_query_params import deserialize_additional_query_params
from .deserialize_mandatory_query_params import deserialize_mandatory_query_params
from .deserialize_relational_query_params import deserialize_relational_query_params
from .deserialize_transaction_query_params import deserialize_transaction_query_params


def deserialize_invoice_query_params(element: ET.Element) -> Optional[InvoiceQueryParams]:
    if element is None:
        return None

    result = InvoiceQueryParams(
        mandatory_query_params=deserialize_mandatory_query_params(
            XR.find_child(element, 'mandatoryQueryParams', API)
        ),
        additional_query_params=deserialize_additional_query_params(
            XR.find_child(element, 'additionalQueryParams', API)
        ),
        relational_query_params=deserialize_relational_query_params(
            XR.find_child(element, 'relationalQueryParams', API)
        ),
        transaction_query_params=deserialize_transaction_query_params(
            XR.find_child(element, 'transactionQueryParams', API)
        ),
    )

    return result
