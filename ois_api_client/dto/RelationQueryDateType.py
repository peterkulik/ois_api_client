from datetime import date
from .QueryOperator import QueryOperator


class RelationQueryDateType:
    """Query parameter for date values

    :param query_operator: Query operator
    :param query_value: Query value
    """

    def __init__(self, query_operator: QueryOperator, query_value: date):
        self.query_operator = query_operator
        self.query_value = query_value
