from datetime import datetime, timezone, tzinfo, timedelta
from typing import Optional
import pytest
import ois_api_client as ois
from ois_api_client.dto.serialization.serialize_header import serialize_header
from ois_api_client.dto.xml.get_full_tag import get_full_tag
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
    data = ois.BasicHeader(request_id=request_id, timestamp=timestamp)
    result = serialize_header(data)

    assert get_full_tag(ois.NAMESPACE_COMMON, 'header') == result.tag

    children = [i for i in result]

    assert 4 == len(children)

    validate_element(children[0], ois.NAMESPACE_COMMON, 'requestId', request_id)
    validate_element(children[1], ois.NAMESPACE_COMMON, 'timestamp', expected_timestamp)
    validate_element(children[2], ois.NAMESPACE_COMMON, 'requestVersion', ois.REQUEST_VERSION)
    validate_element(children[3], ois.NAMESPACE_COMMON, 'headerVersion', ois.HEADER_VERSION)
