from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import API
from ...deserialization.create_enum import create_enum
from ..dto.ProcessingResultList import ProcessingResultList
from ..dto.OriginalRequestVersion import OriginalRequestVersion
from .deserialize_annulment_data import deserialize_annulment_data
from .deserialize_processing_result import deserialize_processing_result


def deserialize_processing_result_list(element: ET.Element) -> Optional[ProcessingResultList]:
    if element is None:
        return None

    result = ProcessingResultList(
        processing_result=[deserialize_processing_result(e) for e in XR.find_all_child(element, 'processingResult', API)],
        original_request_version=create_enum(OriginalRequestVersion, XR.get_child_text(element, 'originalRequestVersion', API)),
        annulment_data=deserialize_annulment_data(
            XR.find_child(element, 'annulmentData', API)
        ),
    )

    return result
