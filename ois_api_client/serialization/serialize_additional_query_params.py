import xml.etree.ElementTree as ET
from typing import Optional

from .serialize_element import serialize_text_element
from ..v3_0 import dto, namespaces as ns


def serialize_additional_query_params(parent: ET.Element, params: dto.AdditionalQueryParams) -> Optional[ET.Element]:
    if params is None:
        return None

    result = ET.SubElement(parent, 'additionalQueryParams')

    serialize_text_element(result, 'taxNumber', params.tax_number, ns.API)
    serialize_text_element(result, 'groupMemberTaxNumber', params.group_member_tax_number, ns.API)
    serialize_text_element(result, 'name', params.name, ns.API)

    if params.invoice_category is not None:
        serialize_text_element(result, 'invoiceCategory', params.invoice_category.value, ns.API)

    if params.payment_method is not None:
        serialize_text_element(result, 'paymentMethod', params.payment_method.value, ns.API)

    if params.invoice_appearance is not None:
        serialize_text_element(result, 'invoiceAppearance', params.invoice_appearance.value, ns.API)

    if params.source is not None:
        serialize_text_element(result, 'source', params.source.value, ns.API)

    serialize_text_element(result, 'currency', params.currency, ns.API)

    return result
