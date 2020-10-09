class UserHeader:
    """Authentication data of the request

    :param login: Login name of the technical user
    :param tax_number: The taxpayer's tax number, whose name the technical user operates in
    """

    def __init__(self, login: str, tax_number: str):
        self.login = login
        self.tax_number = tax_number
