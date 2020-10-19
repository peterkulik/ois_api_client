class AdditionalData:
    """Type for additional data description

    :param data_name: Unique identification of the data field
    :param data_description: Description of content of the data field
    :param data_value: Value of the data
    """

    def __init__(self, data_name: str, data_description: str, data_value: str):
        self.data_name = data_name
        self.data_description = data_description
        self.data_value = data_value
