from typing import Generic, Optional

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
    :param gln_numbers: Global location numbers
    :param material_numbers: Material numbers
    :param item_numbers: Item number(s)
    :param ekaer_ids: EKAER ID-s
    """
    def __init__(self,
                 order_numbers: Optional[OrderNumbers] = None,
                 delivery_notes: Optional[DeliveryNotes] = None,
                 shipping_dates: Optional[ShippingDates] = None,
                 contract_numbers: Optional[ContractNumbers] = None,
                 supplier_company_codes: Optional[SupplierCompanyCodes] = None,
                 customer_company_codes: Optional[CustomerCompanyCodes] = None,
                 dealer_codes: Optional[DealerCodes] = None,
                 cost_centers: Optional[CostCenters] = None,
                 project_numbers: Optional[ProjectNumbers] = None,
                 general_ledger_account_numbers: Optional[GeneralLedgerAccountNumbers] = None,
                 gln_numbers: Optional[GlnNumbers] = None,
                 material_numbers: Optional[MaterialNumbers] = None,
                 item_numbers: Optional[ItemNumbers] = None,
                 ekaer_ids: Optional[EkaerIds] = None
                 ):
        self.order_numbers = order_numbers
        self.delivery_notes = delivery_notes
        self.shipping_dates = shipping_dates
        self.contract_numbers = contract_numbers
        self.supplier_company_codes = supplier_company_codes
        self.customer_company_codes = customer_company_codes
        self.dealer_codes = dealer_codes
        self.cost_centers = cost_centers
        self.project_numbers = project_numbers
        self.general_ledger_account_numbers = general_ledger_account_numbers
        self.gln_numbers = gln_numbers
        self.material_numbers = material_numbers
        self.item_numbers = item_numbers
        self.ekaer_ids = ekaer_ids
