from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import DATA
from ..dto.AggregateInvoiceLineData import AggregateInvoiceLineData


def deserialize_aggregate_invoice_line_data(element: ET.Element) -> Optional[AggregateInvoiceLineData]:
    if element is None:
        return None

    result = AggregateInvoiceLineData(
        line_exchange_rate=XR.get_child_float(element, 'lineExchangeRate', DATA),
        line_delivery_date=XR.get_child_date(element, 'lineDeliveryDate', DATA),
    )

    return result
