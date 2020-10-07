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
    client.query_invoice_digest(data)
