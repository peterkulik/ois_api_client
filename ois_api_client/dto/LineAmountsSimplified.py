from typing import Union


class LineAmountsSimplified:
    """Item value data to be completed in case of simplified invoice

    :param line_gross_amount_simplified:
    :param line_gross_amount_simplified_huf:
    :param line_vat_content:
    """

    def __init__(self,
                 line_gross_amount_simplified: float,
                 line_gross_amount_simplified_huf: float,
                 line_vat_content: Union[float, None] = None):
        self.line_vat_content = line_vat_content
        self.line_gross_amount_simplified = line_gross_amount_simplified
        self.line_gross_amount_simplified_huf = line_gross_amount_simplified_huf
