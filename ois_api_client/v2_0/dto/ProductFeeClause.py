from typing import Optional
from dataclasses import dataclass
from .CustomerDeclaration import CustomerDeclaration
from .ProductFeeTakeoverData import ProductFeeTakeoverData


@dataclass
class ProductFeeClause:
    """Clauses according to the Act LXXXV of 2011 on Environmental Protection Product Fee (related to the item)

    :param product_fee_takeover_data: Data in connection with takeover of environmental protection product fee
    :param customer_declaration: Should the supplier, based on statement given by the purchaser, be exempted from paying product fee, then the product stream affected
    """

    product_fee_takeover_data: Optional[ProductFeeTakeoverData]
    customer_declaration: Optional[CustomerDeclaration]
