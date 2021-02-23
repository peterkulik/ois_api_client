import ois_api_client as ois
from ois_api_client.v2_0 import deserialization, dto
from tests.get_root_dir import get_root_dir
import xml.etree.ElementTree as ET


def test_serialize_general_error_to_object(pytestconfig):
    dir_ = get_root_dir(pytestconfig)

    with open(f'{dir_}/tests/common/exceptions/general_error.xml', 'r') as file:
        general_error_message = file.read()

    general_error = ois.GeneralError(general_error_message)
    root = ET.fromstring(general_error.general_error_response)
    serialized_error = deserialization.deserialize_general_error_response(root)

    assert serialized_error is not None
    assert serialized_error.result is not None

    res = serialized_error.result

    assert res.func_code == dto.FunctionCode.ERROR
    assert res.error_code == 'INVALID_REQUEST'
    assert res.message == 'Helytelen kérés!'

    assert serialized_error.technical_validation_messages is not None

    tvm = serialized_error.technical_validation_messages

    assert len(tvm) == 2
    tvm0 = tvm[0]
    tvm1 = tvm[1]

    assert tvm0.validation_result_code == dto.TechnicalResultCode.ERROR
    assert tvm0.validation_error_code == 'SCHEMA_VIOLATION'
    assert tvm0.message == """Request body contains on line: [1] and column: [23] error: [cvc-elt.1.a: Cannot find the declaration of
            element 'TokenExchangeRequest'.]
        """

    assert tvm1.validation_result_code == dto.TechnicalResultCode.ERROR
    assert tvm1.validation_error_code == 'SCHEMA_VIOLATION'
    assert tvm1.message == """Request body contains on line: [1] and column: [23] error: [unexpected element (uri:"",
            local:"TokenExchangeRequest"). Expected elements are <{http://schemas.nav.gov.hu/OSA/2.0/api}ManageAnnulmentRequest>,<{http://schemas.nav.gov.hu/OSA/2.0/api}ManageInvoiceRequest>,<{http://schemas.nav.gov.hu/OSA/2.0/api}QueryInvoiceChainDigestRequest>,<{http://schemas.nav.gov.hu/OSA/2.0/api}QueryInvoiceCheckRequest>,<{http://schemas.nav.gov.hu/OSA/2.0/api}QueryInvoiceDataRequest>,<{http://schemas.nav.gov.hu/OSA/2.0/api}QueryInvoiceDigestRequest>,<{http://schemas.nav.gov.hu/OSA/2.0/api}QueryTaxpayerRequest>,<{http://schemas.nav.gov.hu/OSA/2.0/api}QueryTransactionListRequest>,<{http://schemas.nav.gov.hu/OSA/2.0/api}QueryTransactionStatusRequest>,<{http://schemas.nav.gov.hu/OSA/2.0/api}TokenExchangeRequest>]
        """
