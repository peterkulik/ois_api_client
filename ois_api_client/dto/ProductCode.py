from typing import Union

from .ProductCodeCategory import ProductCodeCategory


class ProductCodeValue(str):
    """Field type for inputting product codes"""
    pass


class ProductCodeOwnValue(str):
    pass


class ProductCode:
    """Field type including the different product and service codes

    :param product_code_category: The kind of product code (f. ex. VTSZ, CsK, etc.)
    :param product_code_value: ProductCodeValue or ProductCodeOwnValue, product_code_value: The value of (not own) product code, product_code_own_value: Own product code value
    """

    def __init__(self,
                 product_code_category: ProductCodeCategory,
                 product_code_value: Union[ProductCodeValue, ProductCodeOwnValue]):
        self.product_code_category = product_code_category

        if isinstance(product_code_value, ProductCodeValue):
            self.product_code_value = str(product_code_value)
        elif isinstance(product_code_value, ProductCodeOwnValue):
            self.product_code_own_value = str(product_code_value)
