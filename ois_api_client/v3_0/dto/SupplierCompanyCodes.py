from typing import List
from dataclasses import dataclass


@dataclass
class SupplierCompanyCodes:
    """Company codes of the supplier

    :param supplier_company_code: Company code of the supplier
    """

    supplier_company_code: List[str]
