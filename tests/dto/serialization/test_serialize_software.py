from typing import Optional
from datetime import datetime, tzinfo, timedelta
import pytest

from ois_api_client.serialization.serialize_software import serialize_software
from ois_api_client.v3_0 import dto, namespaces as ns
from ois_api_client.xml.get_full_tag import get_full_tag
from tests.dto.serialization.validate_element import validate_element


class HUN(tzinfo):
    def utcoffset(self, dt: Optional[datetime]) -> Optional[timedelta]:
        return timedelta(hours=1)


@pytest.mark.parametrize('id_, name, operation, main_version, dev_name, dev_contact, dev_country_code, dev_tax_number',
                         [
                             ('12345678', 'Super Software', dto.SoftwareOperation.LOCAL_SOFTWARE, 'v1.0', 'John Doe',
                              'john.doe@johndoe.com', 'HU', '12345678'),
                             ('87654321', 'Billing App For Everony', dto.SoftwareOperation.ONLINE_SERVICE, 'v2_0',
                              'John Test', 'john.doe@johndoe.com', None, None),
                             ('87654321', 'Billing App For Everony', dto.SoftwareOperation.ONLINE_SERVICE, 'v2_0',
                              'John Test', 'john.doe@johndoe.com', 'EN', None),
                             ('87654321', 'Billing App For Everony', dto.SoftwareOperation.ONLINE_SERVICE, 'v2_0',
                              'John Test', 'john.doe@johndoe.com', None, '99998888'),
                             ('', '', dto.SoftwareOperation.LOCAL_SOFTWARE, '', '', '', '', '')
                         ])
def test_serialize_software(id_: str, name: str, operation: dto.SoftwareOperation, main_version: str, dev_name: str,
                            dev_contact: str, dev_country_code: str, dev_tax_number: str):
    data = dto.Software(
        software_id=id_,
        software_name=name,
        software_operation=operation,
        software_main_version=main_version,
        software_dev_name=dev_name,
        software_dev_contact=dev_contact,
        software_dev_country_code=dev_country_code,
        software_dev_tax_number=dev_tax_number
    )

    result = serialize_software(data)

    assert get_full_tag(ns.API, 'software') == result.tag

    children = [i for i in result]
    count_of_none_params = 0

    if dev_country_code is None:
        count_of_none_params += 1

    if dev_tax_number is None:
        count_of_none_params += 1

    assert len(children) == 8 - count_of_none_params

    validate_element(children[0], ns.API, 'softwareId', id_)
    validate_element(children[1], ns.API, 'softwareName', name)
    validate_element(children[2], ns.API, 'softwareOperation', operation.value)
    validate_element(children[3], ns.API, 'softwareMainVersion', main_version)
    validate_element(children[4], ns.API, 'softwareDevName', dev_name)
    validate_element(children[5], ns.API, 'softwareDevContact', dev_contact)

    if dev_country_code:
        validate_element(children[6], ns.API, 'softwareDevCountryCode', dev_country_code)

    if dev_tax_number:
        index_of_dev_tax_number = 7 if dev_country_code else 6
        validate_element(children[index_of_dev_tax_number], ns.API, 'softwareDevTaxNumber', dev_tax_number)
