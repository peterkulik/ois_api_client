from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import BASE
from ..namespaces import API
from ...deserialization.create_enum import create_enum
from ..dto.RelationQueryMonetary import RelationQueryMonetary
from ..dto.QueryOperator import QueryOperator


def deserialize_relation_query_monetary(element: ET.Element) -> Optional[RelationQueryMonetary]:
    if element is None:
        return None

    result = RelationQueryMonetary(
        query_operator=create_enum(QueryOperator, XR.get_child_text(element, 'queryOperator', API)),
        query_value=XR.get_child_float(element, 'queryValue', API),
    )

    return result
