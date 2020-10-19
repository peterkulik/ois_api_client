from typing import List, Union

from .Line import Line


class Lines:
    """Product/service data appearing on the invoice

    :param items: Product / service items
    """

    def __init__(self, items: List[Line]):
        self.items = items
