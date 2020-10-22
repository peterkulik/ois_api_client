from typing import List, Union

from .PaymentEvidenceDocumentData import PaymentEvidenceDocumentData
from .ProductFeeData import ProductFeeData
from .ProductFeeOperation import ProductFeeOperation


class ProductFeeSummary:
    """Summary of product charges
    :param product_fee_operation: Indicating whether the the product fee summary concerns refund or deposit
    :param product_fee_data: Product charges data
    :param product_charge_sum: Aggergate product charges
    :param payment_evidence_document_data: Data of the document verifying the declaration submitted on the product fee
    according to the Paragraph (3), Section 13 and the Paragraph (3) Section 25 of the Act LXXXV of 2011
    """

    def __init__(self,
                 product_fee_operation: ProductFeeOperation,
                 product_fee_data: List[ProductFeeData],
                 product_charge_sum: float,
                 payment_evidence_document_data: Union[PaymentEvidenceDocumentData, None] = None):
        self.product_fee_operation = product_fee_operation
        self.product_fee_data = product_fee_data
        self.product_charge_sum = product_charge_sum
        self.payment_evidence_document_data = payment_evidence_document_data
