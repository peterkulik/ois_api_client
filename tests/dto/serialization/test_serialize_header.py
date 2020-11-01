from datetime import datetime, timezone, tzinfo, timedelta
import xml.etree.ElementTree as ET
from typing import Optional

import ois_api_client as ois
from ois_api_client.dto.serialization.serialize_header import serialize_header
from tests.xml import get_full_tag
import pytest


def _validate_element(element: ET.Element, namespace: str, tag_name: str, expected_value: str):
    assert element.tag == get_full_tag(namespace, tag_name)
    assert expected_value == element.text


class HUN(tzinfo):
    def utcoffset(self, dt: Optional[datetime]) -> Optional[timedelta]:
        return timedelta(hours=1)


@pytest.mark.parametrize('request_id, timestamp, expected_timestamp', [
    ('123456789', datetime(2020, 10, 31, 19, 57, 14, 987654, tzinfo=HUN()).astimezone(tz=timezone.utc), '2020-10-31T18:57:14.987Z'),
    ('987654321', datetime(2020, 10, 31, 19, 57, 14, 987654, tzinfo=HUN()), '2020-10-31T18:57:14.987Z'),
    ('123498765', datetime(2020, 10, 31, 19, 57, 14, 987654, tzinfo=timezone.utc), '2020-10-31T19:57:14.987Z')
])
def test_serialize_header(request_id: str, timestamp: datetime, expected_timestamp: str):
    data = ois.BasicHeader(request_id, timestamp)
    result = serialize_header(data)

    assert get_full_tag(ois.NAMESPACE_COMMON, 'header') == result.tag

    children = [i for i in result]

    assert 4 == len(children)

    _validate_element(children[0], ois.NAMESPACE_COMMON, 'requestId', request_id)
    _validate_element(children[1], ois.NAMESPACE_COMMON, 'timestamp', expected_timestamp)
    _validate_element(children[2], ois.NAMESPACE_COMMON, 'requestVersion', ois.REQUEST_VERSION)
    _validate_element(children[3], ois.NAMESPACE_COMMON, 'headerVersion', ois.HEADER_VERSION)
