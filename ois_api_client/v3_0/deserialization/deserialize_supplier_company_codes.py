from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import COMMON
from ..namespaces import DATA
from ..dto.SupplierCompanyCodes import SupplierCompanyCodes


def deserialize_supplier_company_codes(element: ET.Element) -> Optional[SupplierCompanyCodes]:
    if element is None:
        return None

    result = SupplierCompanyCodes(
        supplier_company_code=[e.text for e in XR.find_all_child(element, 'supplierCompanyCode', DATA)],
    )

    return result
