from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import API
from ..dto.RelationalQueryParams import RelationalQueryParams
from .deserialize_relation_query_date import deserialize_relation_query_date
from .deserialize_relation_query_monetary import deserialize_relation_query_monetary


def deserialize_relational_query_params(element: ET.Element) -> Optional[RelationalQueryParams]:
    if element is None:
        return None

    result = RelationalQueryParams(
        invoice_delivery=[deserialize_relation_query_date(e) for e in XR.find_all_child(element, 'invoiceDelivery', API)],
        payment_date=[deserialize_relation_query_date(e) for e in XR.find_all_child(element, 'paymentDate', API)],
        invoice_net_amount=[deserialize_relation_query_monetary(e) for e in XR.find_all_child(element, 'invoiceNetAmount', API)],
        invoice_net_amount_huf=[deserialize_relation_query_monetary(e) for e in XR.find_all_child(element, 'invoiceNetAmountHUF', API)],
        invoice_vat_amount=[deserialize_relation_query_monetary(e) for e in XR.find_all_child(element, 'invoiceVatAmount', API)],
        invoice_vat_amount_huf=[deserialize_relation_query_monetary(e) for e in XR.find_all_child(element, 'invoiceVatAmountHUF', API)],
    )

    return result
