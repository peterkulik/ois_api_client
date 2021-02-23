from dataclasses import dataclass
from .QueryOperator import QueryOperator


@dataclass
class RelationQueryMonetary:
    """Query parameter for monetary values

    :param query_operator: Query operator
    :param query_value: Query value
    """

    query_operator: QueryOperator
    query_value: float
