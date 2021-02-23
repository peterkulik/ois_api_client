from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import API
from ..namespaces import DATA
from ...deserialization.create_enum import create_enum
from ..dto.RelationQueryDate import RelationQueryDate
from ..dto.QueryOperator import QueryOperator


def deserialize_relation_query_date(element: ET.Element) -> Optional[RelationQueryDate]:
    if element is None:
        return None

    result = RelationQueryDate(
        query_operator=create_enum(QueryOperator, XR.get_child_text(element, 'queryOperator', API)),
        query_value=XR.get_child_date(element, 'queryValue', API),
    )

    return result
