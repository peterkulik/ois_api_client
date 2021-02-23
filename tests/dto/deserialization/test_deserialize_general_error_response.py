from typing import Union
import xml.etree.ElementTree as ET
import ois_api_client.v3_0.dto as dto
import ois_api_client.v3_0.deserialization as deserialization
import ois_api_client as ois
from ois_api_client.v3_0 import FunctionCode


def _test_technical_validation_message(
        tvm: Union[dto.TechnicalValidationResult],
        expected_message: str):
    assert tvm.validation_result_code == dto.TechnicalResultCode.ERROR
    assert tvm.validation_error_code == 'SCHEMA_VIOLATION'
    assert tvm.message == expected_message


xml = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<GeneralErrorResponse xmlns="http://schemas.nav.gov.hu/OSA/3.0/api"
                      xmlns:ns2="http://schemas.nav.gov.hu/NTCA/1.0/common"
                      xmlns:ns3="http://schemas.nav.gov.hu/OSA/3.0/base"
                      xmlns:ns4="http://schemas.nav.gov.hu/OSA/3.0/data">
    <ns2:header>
        <ns2:requestId>UniqueId</ns2:requestId>
        <ns2:timestamp>2020-11-08T14:23:12.123Z</ns2:timestamp>
        <ns2:requestVersion>v3_0</ns2:requestVersion>
        <ns2:headerVersion>1.0</ns2:headerVersion>
    </ns2:header>
    <ns2:result>
        <ns2:funcCode>ERROR</ns2:funcCode>
        <ns2:errorCode>INVALID_REQUEST</ns2:errorCode>
        <ns2:message>Helytelen kérés!</ns2:message>
    </ns2:result>
    <software>
        <softwareId>123456789012345678</softwareId>
        <softwareName>Super softwer</softwareName>
        <softwareOperation>LOCAL_SOFTWARE</softwareOperation>
        <softwareMainVersion>1.0</softwareMainVersion>
        <softwareDevName>Super Developer</softwareDevName>
        <softwareDevContact>super@developer.com</softwareDevContact>
        <softwareDevCountryCode>HU</softwareDevCountryCode>
        <softwareDevTaxNumber>12345678</softwareDevTaxNumber>
    </software>
    <technicalValidationMessages>
        <ns2:validationResultCode>ERROR</ns2:validationResultCode>
        <ns2:validationErrorCode>SCHEMA_VIOLATION</ns2:validationErrorCode>
        <ns2:message>Request body contains on line: [1] and column: [123] error: [cvc-elt.1.a: Cannot find the declaration of element 'TokenExchangeRequest'.]</ns2:message>
    </technicalValidationMessages>
    <technicalValidationMessages>
        <ns2:validationResultCode>ERROR</ns2:validationResultCode>
        <ns2:validationErrorCode>SCHEMA_VIOLATION</ns2:validationErrorCode>
        <ns2:message>Request body contains on line: [1] and column: [123] error: [unexpected element (uri:"http://schemas.nav.gov.hu/OSA/2.0/api", local:"TokenExchangeRequest"). Expected elements are &lt;{http://schemas.nav.gov.hu/OSA/3.0/api}ManageAnnulmentRequest&gt;,&lt;{http://schemas.nav.gov.hu/OSA/3.0/api}ManageInvoiceRequest&gt;,&lt;{http://schemas.nav.gov.hu/OSA/3.0/api}QueryInvoiceChainDigestRequest&gt;,&lt;{http://schemas.nav.gov.hu/OSA/3.0/api}QueryInvoiceCheckRequest&gt;,&lt;{http://schemas.nav.gov.hu/OSA/3.0/api}QueryInvoiceDataRequest&gt;,&lt;{http://schemas.nav.gov.hu/OSA/3.0/api}QueryInvoiceDigestRequest&gt;,&lt;{http://schemas.nav.gov.hu/OSA/3.0/api}QueryTaxpayerRequest&gt;,&lt;{http://schemas.nav.gov.hu/OSA/3.0/api}QueryTransactionListRequest&gt;,&lt;{http://schemas.nav.gov.hu/OSA/3.0/api}QueryTransactionStatusRequest&gt;,&lt;{http://schemas.nav.gov.hu/OSA/3.0/api}TokenExchangeRequest&gt;]</ns2:message>
    </technicalValidationMessages>
</GeneralErrorResponse>
"""


def test_deserialize_general_error_response():
    root: ET.Element = ET.fromstring(xml)
    serialized_error = deserialization.deserialize_general_error_response(root)

    assert serialized_error is not None
    assert serialized_error.result is not None

    res = serialized_error.result

    assert res.func_code == FunctionCode.ERROR
    assert res.error_code == 'INVALID_REQUEST'
    assert res.message == 'Helytelen kérés!'

    assert serialized_error.software is not None

    software = serialized_error.software

    assert software.software_id == '123456789012345678'
    assert software.software_name == 'Super softwer'
    assert software.software_operation == ois.v3_0.dto.SoftwareOperation.LOCAL_SOFTWARE
    assert software.software_main_version == '1.0'
    assert software.software_dev_name == 'Super Developer'
    assert software.software_dev_contact == 'super@developer.com'
    assert software.software_dev_country_code == 'HU'
    assert software.software_dev_tax_number == '12345678'

    assert serialized_error.technical_validation_messages is not None

    tvm_list = serialized_error.technical_validation_messages

    assert len(tvm_list) == 2

    _test_technical_validation_message(
        tvm_list[0],
        "Request body contains on line: [1] and column: [123] error: [cvc-elt.1.a: Cannot find the declaration of element 'TokenExchangeRequest'.]")

    _test_technical_validation_message(
        tvm_list[1],
        'Request body contains on line: [1] and column: [123] error: [unexpected element (uri:"http://schemas.nav.gov.hu/OSA/2.0/api", local:"TokenExchangeRequest"). Expected elements are <{http://schemas.nav.gov.hu/OSA/3.0/api}ManageAnnulmentRequest>,<{http://schemas.nav.gov.hu/OSA/3.0/api}ManageInvoiceRequest>,<{http://schemas.nav.gov.hu/OSA/3.0/api}QueryInvoiceChainDigestRequest>,<{http://schemas.nav.gov.hu/OSA/3.0/api}QueryInvoiceCheckRequest>,<{http://schemas.nav.gov.hu/OSA/3.0/api}QueryInvoiceDataRequest>,<{http://schemas.nav.gov.hu/OSA/3.0/api}QueryInvoiceDigestRequest>,<{http://schemas.nav.gov.hu/OSA/3.0/api}QueryTaxpayerRequest>,<{http://schemas.nav.gov.hu/OSA/3.0/api}QueryTransactionListRequest>,<{http://schemas.nav.gov.hu/OSA/3.0/api}QueryTransactionStatusRequest>,<{http://schemas.nav.gov.hu/OSA/3.0/api}TokenExchangeRequest>]')
