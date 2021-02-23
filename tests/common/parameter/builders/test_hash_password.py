from ois_api_client.serialization.hash_password import hash_password
from tests.common import config


def test_hash_password():
    hashed_pw = hash_password(password="super_secret_password_123_*/")
    assert hashed_pw == '3F5D1F340991754CC196F28DA0D48ED38D535A91119C0FDBFD16DA2AB113C24EEFFB0698C979618916C045456E6EA6CD2343C18DECD8C8EE8A9E161F84709D7E'
