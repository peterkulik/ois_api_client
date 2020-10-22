from .ProductCode import ProductCode
from .ProductFeeMeasuringUnit import ProductFeeMeasuringUnit


class ProductFeeData:
    """Product charges data

    :param product_fee_code: Product charges code (Kt or Csk code)
    :param product_fee_quantity: Quantity of product, according to product charge
    :param product_fee_measuring_unit: Unit of the rate (kg or piece)
    :param product_fee_rate: Product fee rate (HUF
    :param product_fee_amount: Amount in Hungarian forints of the product fee
    """

    def __init__(self,
                 product_fee_code: ProductCode,
                 product_fee_quantity: float,
                 product_fee_measuring_unit: ProductFeeMeasuringUnit,
                 product_fee_rate: float,
                 product_fee_amount: float):
        self.product_fee_code = product_fee_code
        self.product_fee_quantity = product_fee_quantity
        self.product_fee_measuring_unit = product_fee_measuring_unit
        self.product_fee_rate = product_fee_rate
        self.product_fee_amount = product_fee_amount
