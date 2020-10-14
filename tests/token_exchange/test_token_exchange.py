import ois_api_client as ois
from tests.common import config


def test_token_exchange():
    client = ois.Client(config.service_url, config.signature_key, config.replacement_key, config.password)

    req: ois.TokenExchangeRequest = ois.TokenExchangeRequest(
        header=ois.BasicHeader(request_id=config.get_request_id(), timestamp=config.get_timestamp()),
        user=config.user,
        software=config.software
    )

    response = client.token_exchange(req)
    assert response is not None
    assert response.result is not None
    assert response.encoded_exchange_token is not None
    assert len(response.encoded_exchange_token) > 0
    assert response.token_validity_from is not None
    assert response.token_validity_to is not None
    assert response.result.error_code is None
    assert response.result.message is None
    assert response.result.func_code == 'OK'
    # err_ser = deserialize_general_error_response(err.general_error_response)
