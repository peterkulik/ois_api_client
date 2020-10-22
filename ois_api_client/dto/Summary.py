from typing import Union, List

from .SummaryGrossData import SummaryGrossData
from .SummaryNormal import SummaryNormal
from .SummarySimplified import SummarySimplified


class Summary:
    """Data of calculation of invoice totals

    :param summary: SummaryNormal or List of SummarySimplified
    SummaryNormal: Calculation of invoice totals (not simplified invoice)
    List of SummarySimplified: Calculation of simplified invoice totals
    :param summary_gross_data: Gross data of the invoice summary
    """

    def __init__(self,
                 summary: Union[SummaryNormal, List[SummarySimplified]],
                 summary_gross_data: Union[SummaryGrossData, None] = None):
        self.summary = summary
        self.summary_gross_data = summary_gross_data
