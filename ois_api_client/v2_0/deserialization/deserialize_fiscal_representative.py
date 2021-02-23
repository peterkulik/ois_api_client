from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import DATA
from ..dto.FiscalRepresentative import FiscalRepresentative
from .deserialize_address import deserialize_address
from .deserialize_tax_number import deserialize_tax_number


def deserialize_fiscal_representative(element: ET.Element) -> Optional[FiscalRepresentative]:
    if element is None:
        return None

    result = FiscalRepresentative(
        fiscal_representative_tax_number=deserialize_tax_number(
            XR.find_child(element, 'fiscalRepresentativeTaxNumber', DATA)
        ),
        fiscal_representative_name=XR.get_child_text(element, 'fiscalRepresentativeName', DATA),
        fiscal_representative_address=deserialize_address(
            XR.find_child(element, 'fiscalRepresentativeAddress', DATA)
        ),
        fiscal_representative_bank_account_number=XR.get_child_text(element, 'fiscalRepresentativeBankAccountNumber', DATA),
    )

    return result
