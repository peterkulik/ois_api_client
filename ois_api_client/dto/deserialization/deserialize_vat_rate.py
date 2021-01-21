import xml.etree.ElementTree as ET
from typing import Optional, Union

from .XmlReader import XmlReader as XR
from ..VatRate import VatRate, VatPercentage, VatExemption, VatOutOfScope, VatDomesticReverseCharge, MarginSchemeVat, \
    MarginSchemeNoVat
from ...constants import NAMESPACE_DATA


def _get_value(element: ET.Element) -> Union[
    VatPercentage,
    VatExemption,
    VatOutOfScope,
    VatDomesticReverseCharge,
    MarginSchemeVat,
    MarginSchemeNoVat
]:
    vat_percentage_el = XR.find_child(element, 'vatPercentage', NAMESPACE_DATA)

    if vat_percentage_el is not None:
        return VatPercentage(XR.get_child_float(element, 'vatPercentage', NAMESPACE_DATA))

    vat_exemption_el = XR.find_child(element, 'vatExemption', NAMESPACE_DATA)

    if vat_exemption_el is not None:
        return VatExemption(XR.get_child_text(element, 'vatExemption', NAMESPACE_DATA))

    vat_out_of_scope_el = XR.find_child(element, 'vatOutOfScope', NAMESPACE_DATA)

    if vat_out_of_scope_el is not None:
        return VatOutOfScope(XR.get_child_bool(element, 'vatOutOfScope', NAMESPACE_DATA, False))

    vat_domestic_reverse_charge_el = XR.find_child(element, 'vatDomesticReverseCharge', NAMESPACE_DATA)

    if vat_domestic_reverse_charge_el is not None:
        return VatDomesticReverseCharge(
            XR.get_child_bool(element, 'vatDomesticReverseCharge', NAMESPACE_DATA, False))

    margin_scheme_vat_el = XR.find_child(element, 'marginSchemeVat', NAMESPACE_DATA)

    if margin_scheme_vat_el is not None:
        return MarginSchemeVat(XR.get_child_bool(element, 'marginSchemeVat', NAMESPACE_DATA, False))

    margin_scheme_no_vat_el = XR.find_child(element, 'marginSchemeNoVat', NAMESPACE_DATA)

    if margin_scheme_no_vat_el is not None:
        return MarginSchemeNoVat(XR.get_child_bool(element, 'marginSchemeNoVat', NAMESPACE_DATA, False))


def deserialize_vat_rate(element: ET.Element) -> Optional[VatRate]:
    if element is None:
        return None

    result = VatRate(_get_value(element))

    return result
