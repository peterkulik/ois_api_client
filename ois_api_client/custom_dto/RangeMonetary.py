from enum import Enum

from ..v3_0.dto.QueryOperator import QueryOperator
from ..v3_0.dto.RelationQueryMonetary import RelationQueryMonetary


class RangeMonetary:
    class FromOperator(Enum):
        """Equals"""
        GT = 'GT'
        """Greater than relation"""
        GTE = 'GTE'

    class ToOperator(Enum):
        """Greater or equals relation"""
        LT = 'LT'
        """Less than relation"""
        LTE = 'LTE'
        """Less or equals relation"""

    def __init__(self, from_operator: FromOperator, from_value: float, to_operator: ToOperator, to_value: float):
        self.relation_query_monetary_list = [
            RelationQueryMonetary(
                query_operator=QueryOperator(from_operator.value),
                query_value=from_value
            ),
            RelationQueryMonetary(
                query_operator=QueryOperator(to_operator.value),
                query_value=to_value
            )]
