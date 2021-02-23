from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import DATA
from ..dto.VatRate import VatRate


def deserialize_vat_rate(element: ET.Element) -> Optional[VatRate]:
    if element is None:
        return None

    result = VatRate(
        vat_percentage=XR.get_child_float(element, 'vatPercentage', DATA),
        vat_exemption=XR.get_child_text(element, 'vatExemption', DATA),
        vat_out_of_scope=XR.get_child_bool(element, 'vatOutOfScope', DATA),
        vat_domestic_reverse_charge=XR.get_child_bool(element, 'vatDomesticReverseCharge', DATA),
        margin_scheme_vat=XR.get_child_bool(element, 'marginSchemeVat', DATA),
        margin_scheme_no_vat=XR.get_child_bool(element, 'marginSchemeNoVat', DATA),
    )

    return result
