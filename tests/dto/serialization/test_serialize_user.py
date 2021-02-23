import pytest
from ois_api_client.serialization.serialize_user import serialize_user
from ois_api_client.v3_0 import dto, namespaces as ns
from ois_api_client.xml.get_full_tag import get_full_tag
from tests.dto.serialization.validate_element import validate_element


@pytest.mark.parametrize(
    'login, tax_number, password_hash, password_hash_type, request_signature, request_signature_type', [
        ('', '', '', '', '', ''),
        ('a', 'b', 'c', 'SHA-512', 'd', 'SHA3-512')
    ])
def test_serialize_user(login: str, tax_number: str, password_hash: str, password_hash_type: str,
                        request_signature: str, request_signature_type: str):
    data = dto.UserHeader(
        login=login,
        password_hash=dto.Crypto(
            value=password_hash,
            crypto_type='shaaa'
        ),
        tax_number=tax_number,
        request_signature=dto.Crypto(
            value=request_signature,
            crypto_type='shaaa'
        )
    )

    result = serialize_user(data=data)

    assert get_full_tag(ns.COMMON, 'user') == result.tag

    children = [i for i in result]

    assert len(children) == 4

    validate_element(children[0], ns.COMMON, 'login', login)
    validate_element(children[1], ns.COMMON, 'passwordHash', password_hash)
    validate_element(children[2], ns.COMMON, 'taxNumber', tax_number)
    validate_element(children[3], ns.COMMON, 'requestSignature', request_signature)
