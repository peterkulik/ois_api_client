from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import DATA
from ..dto.SupplierInfo import SupplierInfo
from .deserialize_address import deserialize_address
from .deserialize_tax_number import deserialize_tax_number


def deserialize_supplier_info(element: ET.Element) -> Optional[SupplierInfo]:
    if element is None:
        return None

    result = SupplierInfo(
        supplier_tax_number=deserialize_tax_number(
            XR.find_child(element, 'supplierTaxNumber', DATA)
        ),
        group_member_tax_number=deserialize_tax_number(
            XR.find_child(element, 'groupMemberTaxNumber', DATA)
        ),
        community_vat_number=XR.get_child_text(element, 'communityVatNumber', DATA),
        supplier_name=XR.get_child_text(element, 'supplierName', DATA),
        supplier_address=deserialize_address(
            XR.find_child(element, 'supplierAddress', DATA)
        ),
        supplier_bank_account_number=XR.get_child_text(element, 'supplierBankAccountNumber', DATA),
        individual_exemption=XR.get_child_bool(element, 'individualExemption', DATA),
        excise_licence_num=XR.get_child_text(element, 'exciseLicenceNum', DATA),
    )

    return result
