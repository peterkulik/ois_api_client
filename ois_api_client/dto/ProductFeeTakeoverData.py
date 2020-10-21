from .Takeover import Takeover


class ProductFeeTakeoverData:
    """Data in connection with takeover of environmental protection product fee

    :param takeover_reason: Direction and legal base of takeover
    :param takeover_amount: Amount in Hungarian forints of the product fee taken over if the purchaser takes over the supplier’s product fee liability
    """

    def __init__(self, takeover_reason: Takeover, takeover_amount: float):
        self.takeover_reason = takeover_reason
        self.takeover_amount = takeover_amount
