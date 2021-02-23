from typing import List
from dataclasses import dataclass
from .ProductCode import ProductCode


@dataclass
class ProductCodes:
    """Product codes

    :param product_code: Product code
    """

    product_code: List[ProductCode]
