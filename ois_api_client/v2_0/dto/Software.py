from typing import Optional
from dataclasses import dataclass
from .SoftwareOperation import SoftwareOperation


@dataclass
class Software:
    """Billing software data

    :param software_id: Billing software ID
    :param software_name: Billing software name
    :param software_operation: Billing software operation type (local program or online billing service)
    :param software_main_version: Billing software main version
    :param software_dev_name: Name of the billing software's developer
    :param software_dev_contact: Electronic contact of the billing software's developer
    :param software_dev_country_code: ISO-3166 alpha2 country code of the billing software's developer
    :param software_dev_tax_number: Tax number of the billing software's developer
    """

    software_id: str
    software_name: str
    software_operation: SoftwareOperation
    software_main_version: str
    software_dev_name: str
    software_dev_contact: str
    software_dev_country_code: Optional[str]
    software_dev_tax_number: Optional[str]
