class Software:
    """Billing software data
    :param id: Billing software ID
    :param name: Billing software name
    :param operation: Billing software operation type (local program or online billing service)
    :param main_version: Billing software main version
    :param dev_name: Name of the billing software's developer
    :param dev_contact: Electronic contact of the billing software's developer
    :param dev_country_code: ISO-3166 alpha2 country code of the billing software's developer
    :param dev_tax_number: Tax number of the billing software's developer
    """

    def __init__(self, id: str, name: str, operation: str, main_version: str, dev_name: str, dev_contact: str,
                 dev_country_code: str, dev_tax_number: str):
        self.id = id
        self.name = name
        self.operation = operation
        self.main_version = main_version
        self.dev_name = dev_name
        self.dev_contact = dev_contact
        self.dev_country_code = dev_country_code
        self.dev_tax_number = dev_tax_number
