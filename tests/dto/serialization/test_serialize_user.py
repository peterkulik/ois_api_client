import pytest
import ois_api_client as ois
from ois_api_client.dto.serialization.serialize_user import serialize_user
from ois_api_client.dto.xml.get_full_tag import get_full_tag
from tests.dto.serialization.validate_element import validate_element


@pytest.mark.parametrize('login, tax_number, password_hash, request_signature', [
    ('', '', '', ''),
    ('a', 'b', 'c', 'd')
])
def test_serialize_user(login: str, tax_number: str, password_hash: str, request_signature: str):
    data = ois.UserHeader(
        login=login,
        tax_number=tax_number
    )

    result = serialize_user(data=data,
                            password_hash=password_hash,
                            request_signature=request_signature)

    assert get_full_tag(ois.NAMESPACE_COMMON, 'user') == result.tag

    children = [i for i in result]

    assert len(children) == 4

    validate_element(children[0], ois.NAMESPACE_COMMON, 'login', login)
    validate_element(children[1], ois.NAMESPACE_COMMON, 'passwordHash', password_hash)
    validate_element(children[2], ois.NAMESPACE_COMMON, 'taxNumber', tax_number)
    validate_element(children[3], ois.NAMESPACE_COMMON, 'requestSignature', request_signature)
