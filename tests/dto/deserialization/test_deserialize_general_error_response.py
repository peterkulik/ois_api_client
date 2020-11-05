import os

import ois_api_client as ois


def _test_technical_validation_message(tvm: ois.TechnicalValidationResult, expected_message: str):
    assert tvm.validation_result_code == 'ERROR'
    assert tvm.validation_error_code == 'SCHEMA_VIOLATION'
    assert tvm.message == expected_message


def test_deserialize_general_error_response():
    path = os.path.join(os.getcwd(), 'general_error.xml')

    with open(path, 'r') as file:
        general_error_message = file.read()

    general_error = ois.GeneralError(general_error_message)
    serialized_error = ois.deserialize_general_error_response(general_error.general_error_response)

    assert serialized_error is not None
    assert serialized_error.result is not None

    res = serialized_error.result

    assert res.func_code == 'ERROR'
    assert res.error_code == 'INVALID_REQUEST'
    assert res.message == 'Helytelen kérés!'

    assert serialized_error.technical_validation_messages is not None

    tvm_list = serialized_error.technical_validation_messages

    assert len(tvm_list) == 2

    _test_technical_validation_message(
        tvm_list[0],
        "Request body contains on line: [1] and column: [123] error: [cvc-elt.1.a: Cannot find the declaration of element 'TokenExchangeRequest'.]")

    _test_technical_validation_message(
        tvm_list[1],
        'Request body contains on line: [1] and column: [123] error: [unexpected element (uri:"http://schemas.nav.gov.hu/OSA/2.0/api", local:"TokenExchangeRequest"). Expected elements are <{http://schemas.nav.gov.hu/OSA/3.0/api}ManageAnnulmentRequest>,<{http://schemas.nav.gov.hu/OSA/3.0/api}ManageInvoiceRequest>,<{http://schemas.nav.gov.hu/OSA/3.0/api}QueryInvoiceChainDigestRequest>,<{http://schemas.nav.gov.hu/OSA/3.0/api}QueryInvoiceCheckRequest>,<{http://schemas.nav.gov.hu/OSA/3.0/api}QueryInvoiceDataRequest>,<{http://schemas.nav.gov.hu/OSA/3.0/api}QueryInvoiceDigestRequest>,<{http://schemas.nav.gov.hu/OSA/3.0/api}QueryTaxpayerRequest>,<{http://schemas.nav.gov.hu/OSA/3.0/api}QueryTransactionListRequest>,<{http://schemas.nav.gov.hu/OSA/3.0/api}QueryTransactionStatusRequest>,<{http://schemas.nav.gov.hu/OSA/3.0/api}TokenExchangeRequest>]')
