import xml.etree.ElementTree as ET
import ois_api_client as ois
from ois_api_client.v3_0 import dto, deserialization
from examples.header_factory import make_headers
from examples.software import software


def test_query_invoice_data():
    client = ois.Client(uri='https://api-test.onlineszamla.nav.gov.hu/invoiceService/v3')

    # These headers (header, user) have to be generated for each call
    header, user_header = make_headers()

    data = dto.QueryInvoiceDataRequest(
        header=header,
        user=user_header,
        software=software,
        invoice_number_query=dto.InvoiceNumberQuery(
            invoice_number='12345678/2020',
            invoice_direction=dto.InvoiceDirection.INBOUND,
            batch_index=None,
            supplier_tax_number='68558132'
        )
    )

    response = client.query_invoice_data(data)

    invoice_data_xml = ois.decode_invoice_data(response.invoice_data_result.invoice_data)
    xml_root = ET.fromstring(invoice_data_xml)
    invoice_data = deserialization.deserialize_invoice_data(xml_root)
