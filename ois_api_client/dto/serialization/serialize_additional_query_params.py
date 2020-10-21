import xml.etree.ElementTree as ET
from typing import Union

from .serialize_element import serialize_text_element
from ..AdditionalQueryParams import AdditionalQueryParams


def serialize_additional_query_params(parent: ET.Element, params: AdditionalQueryParams) -> Union[ET.Element, None]:
    if params is None:
        return None

    result = ET.SubElement(parent, 'additionalQueryParams')

    serialize_text_element(result, 'taxNumber', params.tax_number)
    serialize_text_element(result, 'groupMemberTaxNumber', params.group_member_tax_number)
    serialize_text_element(result, 'name', params.name)

    if params.invoice_category is not None:
        serialize_text_element(result, 'invoiceCategory', params.invoice_category.value)

    if params.payment_method is not None:
        serialize_text_element(result, 'paymentMethod', params.payment_method.value)

    if params.invoice_appearance is not None:
        serialize_text_element(result, 'invoiceAppearance', params.invoice_appearance.value)

    if params.source is not None:
        serialize_text_element(result, 'source', params.source.value)

    serialize_text_element(result, 'currency', params.currency)

    return result
