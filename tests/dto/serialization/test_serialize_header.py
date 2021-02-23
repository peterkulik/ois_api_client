from datetime import datetime, timezone, tzinfo, timedelta
from typing import Optional
import pytest
import ois_api_client as ois
from ois_api_client.v3_0 import dto, namespaces as ns
from ois_api_client.serialization.serialize_header import serialize_header
from ois_api_client.xml.get_full_tag import get_full_tag
from tests.dto.serialization.validate_element import validate_element


class HUN(tzinfo):
    def utcoffset(self, dt: Optional[datetime]) -> Optional[timedelta]:
        return timedelta(hours=1)


@pytest.mark.parametrize('request_id, timestamp, expected_timestamp', [
    ('123456789', datetime(2020, 10, 31, 19, 57, 14, 987654, tzinfo=HUN()).astimezone(tz=timezone.utc),
     '2020-10-31T18:57:14.987Z'),
    ('987654321', datetime(2020, 10, 31, 19, 57, 14, 987654, tzinfo=HUN()), '2020-10-31T18:57:14.987Z'),
    ('123498765', datetime(2020, 10, 31, 19, 57, 14, 987654, tzinfo=timezone.utc), '2020-10-31T19:57:14.987Z')
])
def test_serialize_header(request_id: str, timestamp: datetime, expected_timestamp: str):
    data = dto.BasicHeader(request_id=request_id,
                           timestamp=timestamp,
                           request_version=ois.REQUEST_VERSION,
                           header_version=ois.HEADER_VERSION)
    result = serialize_header(data)

    assert get_full_tag(ns.COMMON, 'header') == result.tag

    children = [i for i in result]

    assert len(children) == 4

    validate_element(children[0], ns.COMMON, 'requestId', request_id)
    validate_element(children[1], ns.COMMON, 'timestamp', expected_timestamp)
    validate_element(children[2], ns.COMMON, 'requestVersion', ois.REQUEST_VERSION)
    validate_element(children[3], ns.COMMON, 'headerVersion', ois.HEADER_VERSION)
