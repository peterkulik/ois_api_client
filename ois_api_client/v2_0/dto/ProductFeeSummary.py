from typing import Optional
from typing import List
from dataclasses import dataclass
from .PaymentEvidenceDocumentData import PaymentEvidenceDocumentData
from .ProductFeeData import ProductFeeData
from .ProductFeeOperation import ProductFeeOperation


@dataclass
class ProductFeeSummary:
    """Summary of product charges

    :param product_fee_operation: Indicating whether the the product fee summary concerns refund or deposit
    :param product_fee_data: Product charges data
    :param product_charge_sum: Aggergate product charges
    :param payment_evidence_document_data: Data of the document verifying the declaration submitted on the product fee according to the Paragraph (3), Section 13 and the Paragraph (3) Section 25 of the Act LXXXV of 2011
    """

    product_fee_operation: ProductFeeOperation
    product_fee_data: List[ProductFeeData]
    product_charge_sum: float
    payment_evidence_document_data: Optional[PaymentEvidenceDocumentData]
