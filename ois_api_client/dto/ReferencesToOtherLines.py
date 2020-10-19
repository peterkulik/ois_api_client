from typing import List


class ReferencesToOtherLines:
    """References to connected items if it is necessary according to VAT law
    
    :param items: References to connected items if it is necessary according to VAT law
    """

    def __init__(self, items: List[int] = None):
        super().__init__()

        if items is None:
            items: List[int] = []
        self.items = items
