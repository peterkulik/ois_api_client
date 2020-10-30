import ois_api_client as ois
import pytest


@pytest.mark.skip(reason='set up correct path')
def test_deserialize_invoice_data():
    with open('normal_invoice.xml', 'r') as file:
        xml = file.read().replace('\n', '')

        invoice_data = ois.deserialize_invoice_data(xml)

        assert invoice_data.invoiceNumber == '12345678/2020'
