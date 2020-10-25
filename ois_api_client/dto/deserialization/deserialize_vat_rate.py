import xml.etree.ElementTree as ET
from typing import Union

from .XmlReader import XmlReader as XR
from ..VatRate import VatRate
from ...constants import NAMESPACE_DATA


def deserialize_vat_rate(element: ET.Element) -> Union[VatRate, None]:
    if element is None:
        return None

    result = VatRate(
        vat_percentage=XR.get_child_float(element, 'vatPercentage', NAMESPACE_DATA),
        vat_exemption=XR.get_child_text(element, 'vatExemption', NAMESPACE_DATA),
        vat_out_of_scope=XR.get_child_bool(element, 'vatOutOfScope', NAMESPACE_DATA, False),
        vat_domestic_reverse_charge=XR.get_child_bool(element, 'vatDomesticReverseCharge', NAMESPACE_DATA, False),
        margin_scheme_vat=XR.get_child_bool(element, 'marginSchemeVat', NAMESPACE_DATA, False),
        margin_scheme_no_vat=XR.get_child_bool(element, 'marginSchemeNoVat', NAMESPACE_DATA, False)
    )

    return result
