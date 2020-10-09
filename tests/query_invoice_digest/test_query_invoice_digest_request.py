from datetime import datetime
import ois_client_sdk as ois
from tests.common import config


def test_query_invoice_digest_request():
    client = ois.Client(config.service_url, config.signature_key, config.replacement_key, config.password)

    data = ois.QueryInvoiceDigestRequest(
        header=ois.BasicHeader(request_id=config.request_id, timestamp=config.timestamp),
        user=config.user,
        software=config.software,
        page=1,
        invoice_direction=ois.InvoiceDirection.INBOUND,
        invoice_query_params=ois.InvoiceQueryParams(
            ois.MandatoryQueryParams(
                ois.MandatoryQueryParams.InsDate(
                    ois.DateTimeIntervalParam(
                        date_time_from=datetime(2020, 10, 1),
                        date_time_to=datetime(2020, 10, 30)
                    ))))
    )
    response = client.query_invoice_digest(data)

    assert response is not None
    assert response.result is not None
    assert response.result.func_code == 'OK'
    assert response.result.message is None
    assert response.result.error_code is None
    assert response.invoice_digest_result is not None
    assert response.invoice_digest_result.current_page == 1
    assert response.invoice_digest_result.available_page == 1
    assert response.invoice_digest_result.invoice_digest is not None
    assert len(response.invoice_digest_result.invoice_digest) > 0
