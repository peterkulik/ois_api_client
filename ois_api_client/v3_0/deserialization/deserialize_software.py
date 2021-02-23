from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import API
from ..namespaces import COMMON
from ...deserialization.create_enum import create_enum
from ..dto.Software import Software
from ..dto.SoftwareOperation import SoftwareOperation


def deserialize_software(element: ET.Element) -> Optional[Software]:
    if element is None:
        return None

    result = Software(
        software_id=XR.get_child_text(element, 'softwareId', API),
        software_name=XR.get_child_text(element, 'softwareName', API),
        software_operation=create_enum(SoftwareOperation, XR.get_child_text(element, 'softwareOperation', API)),
        software_main_version=XR.get_child_text(element, 'softwareMainVersion', API),
        software_dev_name=XR.get_child_text(element, 'softwareDevName', API),
        software_dev_contact=XR.get_child_text(element, 'softwareDevContact', API),
        software_dev_country_code=XR.get_child_text(element, 'softwareDevCountryCode', API),
        software_dev_tax_number=XR.get_child_text(element, 'softwareDevTaxNumber', API),
    )

    return result
