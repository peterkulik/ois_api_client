from typing import Optional

from .TaxNumber import TaxNumber


class CustomerTaxNumber(TaxNumber):
    """Tax number or group identification number, under which the purchase of goods or services is done

    :param taxpayer_id: Core tax number of the taxable person. In case of group taxation arrangement the group
    identification number
    :param vat_code: VAT code to indicate taxation type of the taxpayer. One digit
    :param county_code: County code, two digits
    :param group_member_tax_number: Tax number of group member, when the purchase of goods or services is done under
    group identification number
    """

    def __init__(self,
                 taxpayer_id: str,
                 vat_code: Optional[str],
                 county_code: Optional[str],
                 group_member_tax_number: Optional[TaxNumber]):
        super(CustomerTaxNumber, self).__init__(
            taxpayer_id=taxpayer_id,
            vat_code=vat_code,
            county_code=county_code)
        self.group_member_tax_number = group_member_tax_number
