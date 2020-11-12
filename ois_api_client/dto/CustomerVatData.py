from .CustomerTaxNumber import CustomerTaxNumber


class CustomerVatData:
    """VAT subjectivity data of the customer

    :param customer_tax_number: Domestic tax number or group identification number, under which the purchase of goods or services is done
    :param community_vat_number: Community tax number
    :param third_state_tax_id: Third state tax identification number
    """

    def __init__(self,
                 customer_tax_number: CustomerTaxNumber,
                 community_vat_number: str,
                 third_state_tax_id: str):
        self.customer_tax_number = customer_tax_number
        self.community_vat_number = community_vat_number
        self.third_state_tax_id = third_state_tax_id
