from typing import List

from .ProductCode import ProductCode


class ProductCodes:
    """Product codes

    :param items: Product codes
    """
    def __init__(self, items: List[ProductCode]):
        self.items = items
