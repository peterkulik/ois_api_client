import xml.etree.ElementTree as ET
import ois_api_client as ois
from ois_api_client.v3_0 import dto, deserialization
from examples.header_factory import make_headers
from examples.software import software


def test_token_exchange():
    client = ois.Client(uri='https://api-test.onlineszamla.nav.gov.hu/invoiceService/v3')
    header, user_header = make_headers()

    request = dto.BasicOnlineInvoiceRequest(
        header=header,
        user=user_header,
        software=software
    )

    response = client.token_exchange(request)
    assert response is not None
    assert response.result is not None
    assert response.encoded_exchange_token is not None
    assert len(response.encoded_exchange_token) > 0
    assert response.token_validity_from is not None
    assert response.token_validity_to is not None
    assert response.result.error_code is None
    assert response.result.message is None
    assert response.result.func_code == dto.FunctionCode.OK
