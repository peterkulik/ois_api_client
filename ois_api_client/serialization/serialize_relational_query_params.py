import xml.etree.ElementTree as ET
from datetime import date
from typing import Optional, Union

from .serialize_element import serialize_text_element, serialize_float_element, serialize_date_element
from ois_api_client.custom_dto.RangeDate import RangeDate
from ois_api_client.custom_dto.RangeMonetary import RangeMonetary
from ..v3_0 import dto, namespaces as ns


def _serialize_relation_query_date(parent: ET.Element, value: dto.RelationQueryDate):
    serialize_text_element(parent, 'queryOperator', value.query_operator.value, ns.API)
    serialize_date_element(parent, 'queryValue', value.query_value)


def _serialize_relation_query_monetary(parent: ET.Element, value: dto.RelationQueryMonetary):
    serialize_text_element(parent, 'queryOperator', value.query_operator.value, ns.API)
    serialize_float_element(parent, 'queryValue', value.query_value, 2, ns.API)


def _serialize_query_date_param(parent: ET.Element, tag: str,
                                value: Union[date, RangeDate, dto.RelationQueryDate, None]):
    if value is None:
        return None

    if isinstance(value, date):
        result = ET.SubElement(parent, tag)
        _serialize_relation_query_date(result, dto.RelationQueryDate(
            query_operator=dto.QueryOperator.EQ,
            query_value=value
        ))
    elif isinstance(value, dto.RelationQueryDate):
        result = ET.SubElement(parent, tag)
        _serialize_relation_query_date(result, value)
    elif isinstance(value, RangeDate):
        for relation_query_date in value.relation_query_date_list:
            result = ET.SubElement(parent, tag)
            _serialize_relation_query_date(result, relation_query_date)


def _serialize_query_monetary_param(parent: ET.Element, tag: str,
                                    value: Union[float, RangeMonetary, dto.RelationQueryMonetary, None]):
    if value is None:
        return None

    if isinstance(value, float) or isinstance(value, int):
        result = ET.SubElement(parent, tag)
        _serialize_relation_query_monetary(result, dto.RelationQueryMonetary(
            query_operator=dto.QueryOperator.EQ,
            query_value=value
        ))
    elif isinstance(value, dto.RelationQueryMonetary):
        result = ET.SubElement(parent, tag)
        _serialize_relation_query_monetary(result, value)
    elif isinstance(value, RangeMonetary):
        for relation_query_monetary in value.relation_query_monetary_list:
            result = ET.SubElement(parent, tag)
            _serialize_relation_query_monetary(result, relation_query_monetary)


def serialize_relational_query_params(parent: ET.Element, params: dto.RelationalQueryParams) -> Optional[ET.Element]:
    if params is None:
        return None

    result = ET.SubElement(parent, 'relationalQueryParams')

    _serialize_query_date_param(result, 'invoiceDelivery', params.invoice_delivery)
    _serialize_query_date_param(result, 'paymentDate', params.payment_date)

    _serialize_query_monetary_param(result, 'invoiceNetAmount', params.invoice_net_amount)
    _serialize_query_monetary_param(result, 'invoiceNetAmountHUF', params.invoice_net_amount_huf)

    _serialize_query_monetary_param(result, 'invoiceVatAmount', params.invoice_vat_amount)
    _serialize_query_monetary_param(result, 'invoiceVatAmountHUF', params.invoice_vat_amount_huf)

    return result
