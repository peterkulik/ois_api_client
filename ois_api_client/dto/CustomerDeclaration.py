from decimal import Decimal

from .ProductStream import ProductStream


class CustomerDeclaration:
    """Should the supplier, based on statement given by the purchaser, be exempted from paying product fee, then the product stream affected

    :param product_stream: Product stream
    :param product_fee_weight: Weight of product fee obliged product in kilogram
    """

    def __init__(self, product_stream: ProductStream, product_fee_weight: Decimal):
        self.product_stream = product_stream
        self.product_fee_weight = product_fee_weight
