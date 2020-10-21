from .QueryOperator import QueryOperator


class RelationQueryMonetary:
    """Query parameter for monetary values

    :param query_operator: Query operator
    :param query_value: Query value
    """

    def __init__(self, query_operator: QueryOperator, query_value: float):
        self.query_operator = query_operator
        self.query_value = query_value
