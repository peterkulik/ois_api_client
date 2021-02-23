from dataclasses import dataclass


@dataclass
class AdditionalData:
    """Type for additional data description

    :param data_name: Unique identification of the data field
    :param data_description: Description of content of the data field
    :param data_value: Value of the data
    """

    data_name: str
    data_description: str
    data_value: str
