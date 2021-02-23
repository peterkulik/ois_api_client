from typing import List
from dataclasses import dataclass


@dataclass
class CustomerCompanyCodes:
    """Company codes of the customer

    :param customer_company_code: Company code of the customer
    """

    customer_company_code: List[str]
