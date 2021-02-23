from typing import List
from dataclasses import dataclass


@dataclass
class EkaerIds:
    """EKAER ID-s

    :param ekaer_id: EKAER numbers; EKAER stands for Electronic Trade and Transport Control System
    """

    ekaer_id: List[str]
