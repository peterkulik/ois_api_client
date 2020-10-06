from ois_client_sdk.dto.serialization.build_request_signature import build_request_signature
from tests.common import config
from tests.common.config import expected_request_signature


def test_build_request_signature_without_hash_list_success():
    rs = build_request_signature(config.request_id, config.timestamp, config.signature_key)
    assert rs == expected_request_signature
