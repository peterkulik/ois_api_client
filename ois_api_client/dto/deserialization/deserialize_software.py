import xml.etree.ElementTree as ET
from .XmlReader import XmlReader as XR
from ... import Software
from ...constants import NAMESPACE_API


def deserialize_software(parent: ET.Element):
    if parent is None:
        return None

    res_el = XR.find_child(parent, 'software', NAMESPACE_API)

    if res_el is None:
        return None

    result = Software(
        id=XR.get_child_text(res_el, 'softwareId', NAMESPACE_API),
        name=XR.get_child_text(res_el, 'softwareName', NAMESPACE_API),
        operation=XR.get_child_text(res_el, 'softwareOperation', NAMESPACE_API),
        main_version=XR.get_child_text(res_el, 'softwareMainVersion', NAMESPACE_API),
        dev_name=XR.get_child_text(res_el, 'softwareDevName', NAMESPACE_API),
        dev_contact=XR.get_child_text(res_el, 'softwareDevContact', NAMESPACE_API),
        dev_country_code=XR.get_child_text(res_el, 'softwareDevCountryCode', NAMESPACE_API),
        dev_tax_number=XR.get_child_text(res_el, 'softwareDevTaxNumber', NAMESPACE_API)
    )

    return result
