from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import BASE
from ..namespaces import COMMON
from ..namespaces import DATA
from ..dto.AdvancePaymentData import AdvancePaymentData


def deserialize_advance_payment_data(element: ET.Element) -> Optional[AdvancePaymentData]:
    if element is None:
        return None

    result = AdvancePaymentData(
        advance_original_invoice=XR.get_child_text(element, 'advanceOriginalInvoice', DATA),
        advance_payment_date=XR.get_child_date(element, 'advancePaymentDate', DATA),
        advance_exchange_rate=XR.get_child_float(element, 'advanceExchangeRate', DATA),
    )

    return result
