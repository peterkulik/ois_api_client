from datetime import date
from dataclasses import dataclass
from .QueryOperator import QueryOperator


@dataclass
class RelationQueryDate:
    """Query parameter for date values

    :param query_operator: Query operator
    :param query_value: Query value
    """

    query_operator: QueryOperator
    query_value: date
