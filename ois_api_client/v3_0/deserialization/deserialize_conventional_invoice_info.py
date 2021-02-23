from typing import Optional
import xml.etree.ElementTree as ET
from ...xml.XmlReader import XmlReader as XR
from ..namespaces import DATA
from ..dto.ConventionalInvoiceInfo import ConventionalInvoiceInfo
from .deserialize_contract_numbers import deserialize_contract_numbers
from .deserialize_cost_centers import deserialize_cost_centers
from .deserialize_customer_company_codes import deserialize_customer_company_codes
from .deserialize_dealer_codes import deserialize_dealer_codes
from .deserialize_delivery_notes import deserialize_delivery_notes
from .deserialize_ekaer_ids import deserialize_ekaer_ids
from .deserialize_general_ledger_account_numbers import deserialize_general_ledger_account_numbers
from .deserialize_gln_numbers import deserialize_gln_numbers
from .deserialize_item_numbers import deserialize_item_numbers
from .deserialize_material_numbers import deserialize_material_numbers
from .deserialize_order_numbers import deserialize_order_numbers
from .deserialize_project_numbers import deserialize_project_numbers
from .deserialize_shipping_dates import deserialize_shipping_dates
from .deserialize_supplier_company_codes import deserialize_supplier_company_codes


def deserialize_conventional_invoice_info(element: ET.Element) -> Optional[ConventionalInvoiceInfo]:
    if element is None:
        return None

    result = ConventionalInvoiceInfo(
        order_numbers=deserialize_order_numbers(
            XR.find_child(element, 'orderNumbers', DATA)
        ),
        delivery_notes=deserialize_delivery_notes(
            XR.find_child(element, 'deliveryNotes', DATA)
        ),
        shipping_dates=deserialize_shipping_dates(
            XR.find_child(element, 'shippingDates', DATA)
        ),
        contract_numbers=deserialize_contract_numbers(
            XR.find_child(element, 'contractNumbers', DATA)
        ),
        supplier_company_codes=deserialize_supplier_company_codes(
            XR.find_child(element, 'supplierCompanyCodes', DATA)
        ),
        customer_company_codes=deserialize_customer_company_codes(
            XR.find_child(element, 'customerCompanyCodes', DATA)
        ),
        dealer_codes=deserialize_dealer_codes(
            XR.find_child(element, 'dealerCodes', DATA)
        ),
        cost_centers=deserialize_cost_centers(
            XR.find_child(element, 'costCenters', DATA)
        ),
        project_numbers=deserialize_project_numbers(
            XR.find_child(element, 'projectNumbers', DATA)
        ),
        general_ledger_account_numbers=deserialize_general_ledger_account_numbers(
            XR.find_child(element, 'generalLedgerAccountNumbers', DATA)
        ),
        gln_numbers_supplier=deserialize_gln_numbers(
            XR.find_child(element, 'glnNumbersSupplier', DATA)
        ),
        gln_numbers_customer=deserialize_gln_numbers(
            XR.find_child(element, 'glnNumbersCustomer', DATA)
        ),
        material_numbers=deserialize_material_numbers(
            XR.find_child(element, 'materialNumbers', DATA)
        ),
        item_numbers=deserialize_item_numbers(
            XR.find_child(element, 'itemNumbers', DATA)
        ),
        ekaer_ids=deserialize_ekaer_ids(
            XR.find_child(element, 'ekaerIds', DATA)
        ),
    )

    return result
