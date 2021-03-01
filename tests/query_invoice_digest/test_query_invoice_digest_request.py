from datetime import datetime
import ois_api_client as ois
from ois_api_client.header_factory import make_default_header_factory
from ois_api_client.v3_0 import dto
from tests.common import config
from tests.common.load_params import load_params


def test_query_invoice_digest_request():
    client = ois.Client(uri=config.service_url, timeout=30)

    make_header = make_default_header_factory(load_parameters=load_params)
    header, user = make_header()

    data = dto.QueryInvoiceDigestRequest(
        header=header,
        user=user,
        software=config.software,
        page=1,
        invoice_direction=dto.InvoiceDirection.INBOUND,
        invoice_query_params=dto.InvoiceQueryParams(
            mandatory_query_params=dto.MandatoryQueryParams(
                ins_date=dto.DateTimeIntervalParam(
                    date_time_from=datetime(2020, 10, 1),
                    date_time_to=datetime(2020, 10, 30)
                ),
                invoice_issue_date=None,
                original_invoice_number=None
            ),
            additional_query_params=None,
            relational_query_params=None,
            transaction_query_params=None
        )
    )
    response = client.query_invoice_digest(data)

    assert response is not None
    assert response.result is not None
    assert response.result.func_code == dto.FunctionCode.OK
    assert response.result.message is None
    assert response.result.error_code is None
    assert response.invoice_digest_result is not None
    assert response.invoice_digest_result.current_page == 1
    assert response.invoice_digest_result.available_page == 1
    assert response.invoice_digest_result.invoice_digest is not None
    assert len(response.invoice_digest_result.invoice_digest) > 0
