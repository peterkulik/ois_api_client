from dataclasses import dataclass
from .ProductCodeCategory import ProductCodeCategory


@dataclass
class ProductCode:
    """Field type including the different product and service codes

    :param product_code_category: The kind of product code (f. ex. VTSZ, CsK, etc.)
    :param product_code_value: The value of (not own) product code
    :param product_code_own_value: Own product code value
    """

    product_code_category: ProductCodeCategory
    product_code_value: str
    product_code_own_value: str
