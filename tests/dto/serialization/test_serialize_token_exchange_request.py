from datetime import datetime

import pytest

import ois_api_client as ois
from ois_api_client import NAMESPACE_API
from ois_api_client.dto.serialization.serialize_token_exchange_request import serialize_token_exchange_request
from ois_api_client.dto.xml.get_full_tag import get_full_tag
from tests.dto.serialization.validate_element import validate_element, validate_tag_name


@pytest.mark.parametrize(
    argnames=('request_id', 'timestamp', 'request_signature', 'password_hash', 'login', 'tax_number',
              'software_id', 'software_name', 'software_operation', 'software_main_version',
              'software_dev_name', 'software_dev_contact'),
    argvalues=[
        ('', datetime.now(), '', '', '', '', '', '', ois.SoftwareOperation.LOCAL_SOFTWARE, '', '', '')
    ])
def test_serialize_token_exchange_request(request_id: str, timestamp: datetime, request_signature: str,
                                          password_hash: str, login: str, tax_number: str, software_id: str,
                                          software_name: str, software_operation: ois.SoftwareOperation,
                                          software_main_version: str, software_dev_name: str,
                                          software_dev_contact: str):
    data = ois.TokenExchangeRequest(
        header=ois.BasicHeader(
            request_id=request_id,
            timestamp=timestamp
        ),
        user=ois.UserHeader(
            login=login,
            tax_number=tax_number
        ),
        software=ois.Software(
            id=software_id,
            name=software_name,
            operation=software_operation,
            main_version=software_main_version,
            dev_name=software_dev_name,
            dev_contact=software_dev_contact
        )
    )

    result = serialize_token_exchange_request(data, request_signature, password_hash=password_hash)

    assert get_full_tag(NAMESPACE_API, 'TokenExchangeRequest') == result.tag

    children = [i for i in result]

    assert len(children) == 3

    validate_tag_name(children[0], ois.NAMESPACE_COMMON, 'header')
    validate_tag_name(children[1], ois.NAMESPACE_COMMON, 'user')
    validate_tag_name(children[2], ois.NAMESPACE_API, 'software')
