from typing import List
from dataclasses import dataclass


@dataclass
class EkaerIds:
    """EKAER ID-s of the item

    :param ekaer_id: EKAER number(s) identifying the item; EKAER stands for Electronic Trade and Transport Control System
    """

    ekaer_id: List[str]
