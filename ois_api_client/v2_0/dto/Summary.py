from typing import Optional
from typing import List
from dataclasses import dataclass
from .SummaryGrossData import SummaryGrossData
from .SummaryNormal import SummaryNormal
from .SummarySimplified import SummarySimplified


@dataclass
class Summary:
    """Data of calculation of invoice totals

    :param summary_normal: Calculation of invoice totals (not simplified invoice)
    :param summary_simplified: Calculation of simplified invoice totals
    :param summary_gross_data: Gross data of the invoice summary
    """

    summary_normal: SummaryNormal
    summary_simplified: List[SummarySimplified]
    summary_gross_data: Optional[SummaryGrossData]
