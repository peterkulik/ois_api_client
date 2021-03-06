from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import COMMON
from ..namespaces import DATA
from ..dto.CustomerCompanyCodes import CustomerCompanyCodes


def deserialize_customer_company_codes(element: ET.Element) -> Optional[CustomerCompanyCodes]:
    if element is None:
        return None

    result = CustomerCompanyCodes(
        customer_company_code=[e.text for e in XR.find_all_child(element, 'customerCompanyCode', DATA)],
    )

    return result
