from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import DATA
from ...deserialization.create_enum import create_enum
from ..dto.VatRate import VatRate
from ..dto.MarginScheme import MarginScheme
from .deserialize_detailed_reason import deserialize_detailed_reason
from .deserialize_vat_amount_mismatch import deserialize_vat_amount_mismatch


def deserialize_vat_rate(element: ET.Element) -> Optional[VatRate]:
    if element is None:
        return None

    result = VatRate(
        vat_percentage=XR.get_child_float(element, 'vatPercentage', DATA),
        vat_content=XR.get_child_float(element, 'vatContent', DATA),
        vat_exemption=deserialize_detailed_reason(
            XR.find_child(element, 'vatExemption', DATA)
        ),
        vat_out_of_scope=deserialize_detailed_reason(
            XR.find_child(element, 'vatOutOfScope', DATA)
        ),
        vat_domestic_reverse_charge=XR.get_child_bool(element, 'vatDomesticReverseCharge', DATA),
        margin_scheme_indicator=create_enum(MarginScheme, XR.get_child_text(element, 'marginSchemeIndicator', DATA)),
        vat_amount_mismatch=deserialize_vat_amount_mismatch(
            XR.find_child(element, 'vatAmountMismatch', DATA)
        ),
        no_vat_charge=XR.get_child_bool(element, 'noVatCharge', DATA),
    )

    return result
