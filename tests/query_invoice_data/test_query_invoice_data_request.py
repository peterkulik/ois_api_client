from ois_client_sdk.Client import Client
from ois_client_sdk.dto.BasicHeader import BasicHeader
from ois_client_sdk.dto.InvoiceDirection import InvoiceDirection
from ois_client_sdk.dto.InvoiceNumberQuery import InvoiceNumberQuery
from ois_client_sdk.dto.OriginalRequestVersion import OriginalRequestVersion
from ois_client_sdk.dto.QueryInvoiceDataRequest import QueryInvoiceDataRequest
from ois_client_sdk.dto.Source import Source
from tests.common import config


def test_query_invoice_data_request():
    client = Client(config.service_url, config.signature_key, config.replacement_key, config.password)

    data = QueryInvoiceDataRequest(
        header=BasicHeader(request_id=config.request_id, timestamp=config.timestamp),
        user=config.user,
        software=config.software,
        invoice_number_query=InvoiceNumberQuery(
            invoice_number='2020-01',
            invoice_direction=InvoiceDirection.OUTBOUND,
            batch_index=None,
            supplier_tax_number=None
        )
    )
    response = client.query_invoice_data(data)

    assert response is not None
    assert response.result is not None
    assert response.result.func_code == 'OK'
    assert response.result.message is None
    assert response.result.error_code is None
    assert response.invoice_data_result is not None
    assert not response.invoice_data_result.compressed_content_indicator
    assert response.invoice_data_result.invoice_data is not None
    assert response.invoice_data_result.audit_data is not None
    assert response.invoice_data_result.audit_data.ins_date is not None
    assert response.invoice_data_result.audit_data.batch_index is None
    assert response.invoice_data_result.audit_data.index is not None
    assert response.invoice_data_result.audit_data.ins_cus_user is not None
    assert response.invoice_data_result.audit_data.source == Source.XML
    assert response.invoice_data_result.audit_data.original_request_version == OriginalRequestVersion.v_2_0
    assert response.invoice_data_result.audit_data.transaction_id is not None
