import xml.etree.ElementTree as ET
from typing import Union

from .XmlReader import XmlReader as XR
from .deserialize_address import deserialize_address
from .deserialize_tax_number import deserialize_tax_number
from ..FiscalRepresentative import FiscalRepresentative
from ...constants import NAMESPACE_DATA


def deserialize_fiscal_representative_info(element: ET.Element) -> Union[FiscalRepresentative, None]:
    if element is None:
        return None

    result = FiscalRepresentative(
        fiscal_representative_tax_number=deserialize_tax_number(
            XR.find_child(element, 'fiscalRepresentativeTaxNumber', NAMESPACE_DATA)),
        fiscal_representative_name=XR.get_child_text(element, 'fiscalRepresentativeName', NAMESPACE_DATA),
        fiscal_representative_address=deserialize_address(
            XR.find_child(element, 'fiscalRepresentativeAddress', NAMESPACE_DATA)),
        fiscal_representative_bank_account_number=XR.get_child_text(element, 'fiscalRepresentativeBankAccountNumber',
                                                                    NAMESPACE_DATA)
    )

    return result
