import xml.etree.ElementTree as ET
import ois_api_client as ois
from ois_api_client.header_factory import make_default_header_factory
from ois_api_client.v3_0 import dto, deserialization
from tests.common import config
from tests.common.load_params import load_params


def test_query_invoice_data_request():
    client = ois.Client(config.service_url)

    make_header = make_default_header_factory(load_parameters=load_params)
    header, user = make_header()

    data = dto.QueryInvoiceDataRequest(
        header=header,
        user=user,
        software=config.software,
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

    assert response is not None
    assert response.result is not None
    assert response.result.func_code == dto.FunctionCode.OK
    assert response.result.message is None
    assert response.result.error_code is None
    assert response.invoice_data_result is not None
    assert not response.invoice_data_result.compressed_content_indicator
    assert response.invoice_data_result.invoice_data is not None
    assert response.invoice_data_result.audit_data is not None
    assert response.invoice_data_result.audit_data.insdate is not None
    assert response.invoice_data_result.audit_data.batch_index is None
    assert response.invoice_data_result.audit_data.index is not None
    assert response.invoice_data_result.audit_data.ins_cus_user is not None
    assert response.invoice_data_result.audit_data.source == dto.Source.XML
    assert response.invoice_data_result.audit_data.original_request_version == dto.OriginalRequestVersion.O_2_0
    assert response.invoice_data_result.audit_data.transaction_id is not None

    assert invoice_data is not None
