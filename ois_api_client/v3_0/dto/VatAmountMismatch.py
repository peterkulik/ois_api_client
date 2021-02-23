from dataclasses import dataclass


@dataclass
class VatAmountMismatch:
    """Data of mismatching tax base and levied tax

    :param vat_rate: VAT rate, VAT content
    :param case: Case notation with code
    """

    vat_rate: float
    case: str
