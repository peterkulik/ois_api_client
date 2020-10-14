import ois_api_client as ois
from tests.common import config
from tests.common.config import expected_request_signature


def test_build_request_signature_without_hash_list_success():
    rs = ois.build_request_signature(config.get_request_id(), config.get_timestamp(), config.signature_key)
    assert rs == expected_request_signature
