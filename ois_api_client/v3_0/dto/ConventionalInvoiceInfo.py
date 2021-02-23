from typing import Optional
from dataclasses import dataclass
from .ContractNumbers import ContractNumbers
from .CostCenters import CostCenters
from .CustomerCompanyCodes import CustomerCompanyCodes
from .DealerCodes import DealerCodes
from .DeliveryNotes import DeliveryNotes
from .EkaerIds import EkaerIds
from .GeneralLedgerAccountNumbers import GeneralLedgerAccountNumbers
from .GlnNumbers import GlnNumbers
from .ItemNumbers import ItemNumbers
from .MaterialNumbers import MaterialNumbers
from .OrderNumbers import OrderNumbers
from .ProjectNumbers import ProjectNumbers
from .ShippingDates import ShippingDates
from .SupplierCompanyCodes import SupplierCompanyCodes


@dataclass
class ConventionalInvoiceInfo:
    """Other conventionally named data to assist in invoice processing

    :param order_numbers: Order numbers
    :param delivery_notes: Delivery notes
    :param shipping_dates: Shipping dates
    :param contract_numbers: Contract numbers
    :param supplier_company_codes: Company codes of the supplier
    :param customer_company_codes: Company codes of the customer
    :param dealer_codes: Dealer codes
    :param cost_centers: Cost centers
    :param project_numbers: Project numbers
    :param general_ledger_account_numbers: General ledger account numbers
    :param gln_numbers_supplier: Supplier's global location numbers
    :param gln_numbers_customer: Customer's global location numbers
    :param material_numbers: Material numbers
    :param item_numbers: Item number(s)
    :param ekaer_ids: EKAER ID-s
    """

    order_numbers: Optional[OrderNumbers]
    delivery_notes: Optional[DeliveryNotes]
    shipping_dates: Optional[ShippingDates]
    contract_numbers: Optional[ContractNumbers]
    supplier_company_codes: Optional[SupplierCompanyCodes]
    customer_company_codes: Optional[CustomerCompanyCodes]
    dealer_codes: Optional[DealerCodes]
    cost_centers: Optional[CostCenters]
    project_numbers: Optional[ProjectNumbers]
    general_ledger_account_numbers: Optional[GeneralLedgerAccountNumbers]
    gln_numbers_supplier: Optional[GlnNumbers]
    gln_numbers_customer: Optional[GlnNumbers]
    material_numbers: Optional[MaterialNumbers]
    item_numbers: Optional[ItemNumbers]
    ekaer_ids: Optional[EkaerIds]
