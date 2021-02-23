from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import API
from ..namespaces import DATA
from ...deserialization.create_enum import create_enum
from ..dto.AuditData import AuditData
from ..dto.Source import Source
from ..dto.OriginalRequestVersion import OriginalRequestVersion


def deserialize_audit_data(element: ET.Element) -> Optional[AuditData]:
    if element is None:
        return None

    result = AuditData(
        insdate=XR.get_child_datetime(element, 'insdate', API),
        ins_cus_user=XR.get_child_text(element, 'insCusUser', API),
        source=create_enum(Source, XR.get_child_text(element, 'source', API)),
        transaction_id=XR.get_child_text(element, 'transactionId', API),
        index=XR.get_child_int(element, 'index', API),
        batch_index=XR.get_child_int(element, 'batchIndex', API),
        original_request_version=create_enum(OriginalRequestVersion, XR.get_child_text(element, 'originalRequestVersion', API)),
    )

    return result
