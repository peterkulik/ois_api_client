import xml.etree.ElementTree as ET
from typing import Union

from .XmlReader import XmlReader as XR
from .deserialize_address import deserialize_address
from .deserialize_tax_number import deserialize_tax_number
from ..SupplierInfo import SupplierInfo
from ...constants import NAMESPACE_DATA


def deserialize_supplier_info(element: ET.Element) -> Union[SupplierInfo, None]:
    if element is None:
        return None

    result = SupplierInfo(
        supplier_tax_number=deserialize_tax_number(XR.find_child(element, 'supplierTaxNumber', NAMESPACE_DATA)),
        supplier_name=XR.get_child_text(element, 'supplierName', NAMESPACE_DATA),
        supplier_address=deserialize_address(XR.find_child(element, 'supplierAddress', NAMESPACE_DATA)),
        group_member_tax_number=deserialize_tax_number(XR.find_child(element, 'groupMemberTaxNumber', NAMESPACE_DATA)),
        community_vat_number=XR.get_child_text(element, 'communityVatNumber', NAMESPACE_DATA),
        supplier_bank_account_number=XR.get_child_text(element, 'supplierBankAccountNumber', NAMESPACE_DATA),
        individual_exemption=XR.get_child_bool(element, 'individualExemption', NAMESPACE_DATA),
        excise_licence_num=XR.get_child_text(element, 'exciseLicenceNum', NAMESPACE_DATA)
    )

    return result
