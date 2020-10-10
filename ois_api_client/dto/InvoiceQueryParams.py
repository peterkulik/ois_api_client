from .AdditionalQueryParams import AdditionalQueryParams
from .MandatoryQueryParams import MandatoryQueryParams
from .RelationalQueryParams import RelationalQueryParams
from .TransactionQueryParams import TransactionQueryParams


class InvoiceQueryParams:
    """Invoice query parameters

    :param mandatory_query_params: Mandatory params of the invoice query
    :param additional_query_params: Additional params of the invoice query
    :param relational_query_params: Relational params of the invoice query
    :param transaction_query_params: Transactional params of the invoice query
    """

    def __init__(self, mandatory_query_params: MandatoryQueryParams,
                 additional_query_params: AdditionalQueryParams = None,
                 relational_query_params: RelationalQueryParams = None,
                 transaction_query_params: TransactionQueryParams = None):
        self.mandatory_query_params = mandatory_query_params
        self.additional_query_params = additional_query_params
        self.relational_query_params = relational_query_params
        self.transaction_query_params = transaction_query_params
