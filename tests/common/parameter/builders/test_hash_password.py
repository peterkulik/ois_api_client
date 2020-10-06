from ois_client_sdk.dto.serialization.hash_password import hash_password
from tests.common import config


def test_hash_password():
    hashed_pw = hash_password(password=config.password)
    assert hashed_pw == config.expected_password_hash
