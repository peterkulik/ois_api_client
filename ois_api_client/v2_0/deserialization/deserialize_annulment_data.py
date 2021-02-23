from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import API
from ..namespaces import DATA
from ...deserialization.create_enum import create_enum
from ..dto.AnnulmentData import AnnulmentData
from ..dto.AnnulmentVerificationStatus import AnnulmentVerificationStatus


def deserialize_annulment_data(element: ET.Element) -> Optional[AnnulmentData]:
    if element is None:
        return None

    result = AnnulmentData(
        annulment_verification_status=create_enum(AnnulmentVerificationStatus, XR.get_child_text(element, 'annulmentVerificationStatus', API)),
        annulment_decision_date=XR.get_child_datetime(element, 'annulmentDecisionDate', API),
        annulment_decision_user=XR.get_child_text(element, 'annulmentDecisionUser', API),
    )

    return result
