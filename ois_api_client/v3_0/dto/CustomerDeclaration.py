from typing import Optional
from dataclasses import dataclass
from .ProductStream import ProductStream


@dataclass
class CustomerDeclaration:
    """Should the supplier, based on statement given by the purchaser, be exempted from paying product fee, then the product stream affected

    :param product_stream: Product stream
    :param product_fee_weight: Weight of product fee obliged product in kilogram
    """

    product_stream: ProductStream
    product_fee_weight: Optional[float]
