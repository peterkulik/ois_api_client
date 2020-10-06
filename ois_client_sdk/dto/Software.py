from dataclasses import dataclass


@dataclass
class Software:
    id: str
    name: str
    operation: str
    main_version: str
    dev_name: str
    dev_contact: str
    dev_country_code: str
    dev_tax_number: str
