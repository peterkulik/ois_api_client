from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import COMMON
from ..namespaces import DATA
from ..dto.GeneralLedgerAccountNumbers import GeneralLedgerAccountNumbers


def deserialize_general_ledger_account_numbers(element: ET.Element) -> Optional[GeneralLedgerAccountNumbers]:
    if element is None:
        return None

    result = GeneralLedgerAccountNumbers(
        general_ledger_account_number=[e.text for e in XR.find_all_child(element, 'generalLedgerAccountNumber', DATA)],
    )

    return result
