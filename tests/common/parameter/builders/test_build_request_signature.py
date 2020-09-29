from datetime import datetime, timezone

from ois_client_sdk.common.parameter.builders.build_request_signature import build_request_signature
from tests.common.parameter import config


def get_local_timezone():
    return datetime.now().astimezone().tzinfo


def test_build_request_signature_without_hash_list_success():
    request_id = '202092993525132'
    timestamp = datetime(2020, 9, 29, 9, 35, 25, 132000, tzinfo=get_local_timezone())

    rs = build_request_signature(request_id, timestamp, config.signature_key)
    assert rs == '51EC5ABA9140BCB1927195CDF4E0FA3BA3F57E153B95FE7FADFA103F84FD8CF8AB62B321EDC17E02123896150B463A16A50E56494FAC39058D0B6226B03A484F'
