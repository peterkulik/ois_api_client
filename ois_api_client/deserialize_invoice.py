import xml.etree.ElementTree as ET
from typing import Callable, Dict, Union

from .deserialization.decode_invoice_data import decode_invoice_data
from .v3_0 import dto

from .v3_0 import dto as dto_3_0
from .v2_0 import dto as dto_2_0
from .v3_0 import deserialization as des_3_0
from .v2_0 import deserialization as des_2_0

deserialization_mapping: Dict[
    dto.OriginalRequestVersion, Callable[[ET.Element], Union[dto_2_0.InvoiceData, dto_3_0.InvoiceData]]] = {
    dto.OriginalRequestVersion.O_3_0: des_3_0.deserialize_invoice_data,
    dto.OriginalRequestVersion.O_2_0: des_2_0.deserialize_invoice_data
}


def deserialize_invoice(query_invoice_data_response: dto.QueryInvoiceDataResponse) -> Union[
    dto_2_0.InvoiceData, dto_3_0.InvoiceData]:
    res = query_invoice_data_response.invoice_data_result
    req_version = res.audit_data.original_request_version

    if req_version not in deserialization_mapping:
        raise TypeError(f'Not supported invoice request version {req_version}')

    xml = decode_invoice_data(res.invoice_data)
    root = ET.fromstring(xml)
    return deserialization_mapping[req_version](root)
