from datetime import datetime, timedelta

from ois_client_sdk.Client import Client
from ois_client_sdk.dto.BasicHeader import BasicHeader
from ois_client_sdk.dto.DateTimeIntervalParam import DateTimeIntervalParam
from ois_client_sdk.dto.InvoiceDirection import InvoiceDirection
from ois_client_sdk.dto.InvoiceQueryParams import InvoiceQueryParams
from ois_client_sdk.dto.MandatoryQueryParams import MandatoryQueryParams
from ois_client_sdk.dto.QueryInvoiceDigestRequest import QueryInvoiceDigestRequest
from tests.common import config


def test_query_invoice_digest_request():
    client = Client(config.service_url, config.signature_key, config.replacement_key, config.password)

    data = QueryInvoiceDigestRequest(
        header=BasicHeader(request_id=config.request_id, timestamp=config.timestamp),
        user=config.user,
        software=config.software,
        page=1,
        invoice_direction=InvoiceDirection.OUTBOUND,
        invoice_query_params=InvoiceQueryParams(
            MandatoryQueryParams(
                MandatoryQueryParams.InsDate(
                    DateTimeIntervalParam(
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
