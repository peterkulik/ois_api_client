from typing import Optional
from datetime import datetime, tzinfo, timedelta
import pytest
import ois_api_client as ois
from ois_api_client.dto.serialization.serialize_software import serialize_software
from ois_api_client.dto.xml.get_full_tag import get_full_tag
from tests.dto.serialization.validate_element import validate_element


class HUN(tzinfo):
    def utcoffset(self, dt: Optional[datetime]) -> Optional[timedelta]:
        return timedelta(hours=1)


@pytest.mark.parametrize('id_, name, operation, main_version, dev_name, dev_contact, dev_country_code, dev_tax_number',
                         [
                             ('12345678', 'Super Software', ois.SoftwareOperation.LOCAL_SOFTWARE, 'v1.0', 'John Doe',
                              'john.doe@johndoe.com', 'HU', '12345678'),
                             ('87654321', 'Billing App For Everony', ois.SoftwareOperation.ONLINE_SERVICE, 'v2.0',
                              'John Test', 'john.doe@johndoe.com', None, None),
                             ('87654321', 'Billing App For Everony', ois.SoftwareOperation.ONLINE_SERVICE, 'v2.0',
                              'John Test', 'john.doe@johndoe.com', 'EN', None),
                             ('87654321', 'Billing App For Everony', ois.SoftwareOperation.ONLINE_SERVICE, 'v2.0',
                              'John Test', 'john.doe@johndoe.com', None, '99998888'),
                             ('', '', ois.SoftwareOperation.LOCAL_SOFTWARE, '', '', '', '', '')
                         ])
def test_serialize_software(id_: str, name: str, operation: ois.SoftwareOperation, main_version: str, dev_name: str,
                            dev_contact: str, dev_country_code: str, dev_tax_number: str):
    data = ois.Software(
        id=id_,
        name=name,
        operation=operation,
        main_version=main_version,
        dev_name=dev_name,
        dev_contact=dev_contact,
        dev_country_code=dev_country_code,
        dev_tax_number=dev_tax_number
    )

    result = serialize_software(data)

    assert get_full_tag(ois.NAMESPACE_API, 'software') == result.tag

    children = [i for i in result]
    count_of_none_params = 0

    if dev_country_code is None:
        count_of_none_params += 1

    if dev_tax_number is None:
        count_of_none_params += 1

    assert 8 - count_of_none_params == len(children)

    validate_element(children[0], ois.NAMESPACE_API, 'softwareId', id_)
    validate_element(children[1], ois.NAMESPACE_API, 'softwareName', name)
    validate_element(children[2], ois.NAMESPACE_API, 'softwareOperation', operation.value)
    validate_element(children[3], ois.NAMESPACE_API, 'softwareMainVersion', main_version)
    validate_element(children[4], ois.NAMESPACE_API, 'softwareDevName', dev_name)
    validate_element(children[5], ois.NAMESPACE_API, 'softwareDevContact', dev_contact)

    if dev_country_code:
        validate_element(children[6], ois.NAMESPACE_API, 'softwareDevCountryCode', dev_country_code)

    if dev_tax_number:
        index_of_dev_tax_number = 7 if dev_country_code else 6
        validate_element(children[index_of_dev_tax_number], ois.NAMESPACE_API, 'softwareDevTaxNumber', dev_tax_number)
