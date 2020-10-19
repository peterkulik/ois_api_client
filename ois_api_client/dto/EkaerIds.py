from typing import List


class EkaerIds:
    """EKAER ID-s of the item

    :param items: EKAER number(s) identifying the item; EKAER stands for Electronic Trade and Transport Control System"""

    def __init__(self, items: List[str]):
        self.item = items
