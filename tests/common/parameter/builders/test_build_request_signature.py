import ois_api_client as ois
import pytest
from tests.common import config


@pytest.mark.skip(reason='use fix timestamp')
def test_build_request_signature_without_hash_list_success():
    rs = ois.build_request_signature(config.get_request_id(), config.get_timestamp(), config.signature_key)
    assert rs == config.expected_request_signature
