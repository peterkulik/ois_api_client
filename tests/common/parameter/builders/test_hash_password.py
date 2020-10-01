from ois_client_sdk.common.parameter.builders.hash_password import hash_password
from tests.common.parameter import config


def test_hash_password():
    hashed_pw = hash_password(password=config.password)
    assert hashed_pw == config.expected_password_hash
