from typing import Optional
from dataclasses import dataclass
from .AdditionalQueryParams import AdditionalQueryParams
from .MandatoryQueryParams import MandatoryQueryParams
from .RelationalQueryParams import RelationalQueryParams
from .TransactionQueryParams import TransactionQueryParams


@dataclass
class InvoiceQueryParams:
    """Invoice query parameters

    :param mandatory_query_params: Mandatory params of the invoice query
    :param additional_query_params: Additional params of the invoice query
    :param relational_query_params: Relational params of the invoice query
    :param transaction_query_params: Transactional params of the invoice query
    """

    mandatory_query_params: MandatoryQueryParams
    additional_query_params: Optional[AdditionalQueryParams]
    relational_query_params: Optional[RelationalQueryParams]
    transaction_query_params: Optional[TransactionQueryParams]
