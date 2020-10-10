import ois_client_sdk as ois
from tests.common import config


def test_hash_password():
    hashed_pw = ois.hash_password(password=config.password)
    assert hashed_pw == config.expected_password_hash
