from ois_api_client.v2_0 import deserialization
import xml.etree.ElementTree as ET

from tests.get_root_dir import get_root_dir


def test_deserialize_invoice_data(pytestconfig):
    dir_ = get_root_dir(pytestconfig)

    with open(f'{dir_}/tests/query_invoice_data/normal_invoice.xml', 'r') as file:
        xml = file.read().replace('\n', '')

        invoice_data = deserialization.deserialize_invoice_data(ET.fromstring(xml))

        assert invoice_data.invoice_number == '12345678/2020'
