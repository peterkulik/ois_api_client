from datetime import datetime

import pytest

import ois_api_client as ois
from ois_api_client.serialization.serialize_token_exchange_request import serialize_token_exchange_request
from ois_api_client.v3_0 import dto, namespaces as ns
from ois_api_client.xml.get_full_tag import get_full_tag
from tests.dto.serialization.validate_element import validate_tag_name


@pytest.mark.parametrize(
    argnames=('request_id', 'timestamp', 'request_signature', 'password_hash', 'login', 'tax_number',
              'software_id', 'software_name', 'software_operation', 'software_main_version',
              'software_dev_name', 'software_dev_contact'),
    argvalues=[
        ('', datetime.now(), '', '', '', '', '', '', dto.SoftwareOperation.LOCAL_SOFTWARE, '', '', '')
    ])
def test_serialize_token_exchange_request(request_id: str, timestamp: datetime, request_signature: str,
                                          password_hash: str, login: str, tax_number: str, software_id: str,
                                          software_name: str, software_operation: dto.SoftwareOperation,
                                          software_main_version: str, software_dev_name: str,
                                          software_dev_contact: str):

    data = dto.BasicOnlineInvoiceRequest(
        header=dto.BasicHeader(
            request_id=request_id,
            timestamp=timestamp,
            request_version=ois.REQUEST_VERSION,
            header_version=ois.HEADER_VERSION
        ),
        user=dto.UserHeader(
            login=login,
            tax_number=tax_number,
            request_signature=dto.Crypto(
                value=request_signature,
                crypto_type='shaaaaa'
            ),
            password_hash=dto.Crypto(
                value=password_hash,
                crypto_type='shhaaaa'
            )
        ),
        software=dto.Software(
            software_id=software_id,
            software_name=software_name,
            software_operation=software_operation,
            software_main_version=software_main_version,
            software_dev_name=software_dev_name,
            software_dev_contact=software_dev_contact,
            software_dev_country_code=None,
            software_dev_tax_number=None
        )
    )

    result = serialize_token_exchange_request(data)

    assert get_full_tag(ns.API, 'TokenExchangeRequest') == result.tag

    children = [i for i in result]

    assert len(children) == 3

    validate_tag_name(children[0], ns.COMMON, 'header')
    validate_tag_name(children[1], ns.COMMON, 'user')
    validate_tag_name(children[2], ns.API, 'software')
