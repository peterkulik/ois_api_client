from typing import List, Union

from .Line import Line


class Lines:
    """Product/service data appearing on the invoice

    :param merged_item_indicator: Indicates whether the data exchange contains merged line data due to size reduction
    :param items: Product / service items
    """

    def __init__(self,
                 merged_item_indicator: bool,
                 items: List[Line]):
        self.merged_item_indicator = merged_item_indicator
        self.items = items
