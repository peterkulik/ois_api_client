import ois_api_client as ois
from ois_api_client.header_factory import make_default_header_factory
from ois_api_client.v3_0 import dto
from tests.common import config
from tests.common.load_params import load_params


def test_token_exchange():
    client = ois.Client(uri=config.service_url, timeout=30)

    make_header = make_default_header_factory(load_parameters=load_params)
    header, user = make_header()

    request = dto.BasicOnlineInvoiceRequest(
        header=header,
        user=user,
        software=config.software
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
