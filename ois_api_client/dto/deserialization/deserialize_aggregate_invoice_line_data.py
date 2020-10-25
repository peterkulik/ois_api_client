import xml.etree.ElementTree as ET
from typing import Union

from .XmlReader import XmlReader as XR
from ..AggregateInvoiceLineData import AggregateInvoiceLineData
from ...constants import NAMESPACE_DATA


def deserialize_aggregate_invoice_line_data(element: ET.Element) -> Union[AggregateInvoiceLineData, None]:
    if element is None:
        return None

    result = AggregateInvoiceLineData(
        line_delivery_date=XR.get_child_date(element, 'lineDeliveryDate', NAMESPACE_DATA),
        line_exchange_rate=XR.get_child_float(element, 'lineExchangeRate', NAMESPACE_DATA)
    )

    return result


