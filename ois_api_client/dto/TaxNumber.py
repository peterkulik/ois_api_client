from typing import Union


class TaxNumber:
    """Tax number type

    :param taxpayer_id: Core tax number of the taxable person. In case of group taxation arrangement the group
    identification number
    :param vat_code: VAT code to indicate taxation type of the taxpayer. One digit
    :param county_code: County code, two digits
    """

    def __init__(self,
                 taxpayer_id: str,
                 vat_code: Union[str, None] = None,
                 county_code: Union[str, None] = None):
        self.taxpayer_id = taxpayer_id
        self.vat_code = vat_code
        self.county_code = county_code
