import ois_client_sdk as ois
from tests.common import config
from tests.common.config import expected_request_signature


def test_build_request_signature_without_hash_list_success():
    rs = ois.build_request_signature(config.request_id, config.timestamp, config.signature_key)
    assert rs == expected_request_signature
