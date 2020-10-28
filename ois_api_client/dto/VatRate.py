from typing import Union


class VatPercentage(float):
    pass


class VatExemption(str):
    pass


class VatOutOfScope:
    def __init__(self, value: bool):
        self.value = value

    def __bool__(self):
        return self.value


class VatDomesticReverseCharge:
    def __init__(self, value: bool):
        self.value = value

    def __bool__(self):
        return self.value


class MarginSchemeVat:
    def __init__(self, value: bool):
        self.value = value

    def __bool__(self):
        return self.value


class MarginSchemeNoVat:
    def __init__(self, value: bool):
        self.value = value

    def __bool__(self):
        return self.value


class VatRate:
    def __init__(self, value=Union[
        VatPercentage,
        VatExemption,
        VatOutOfScope,
        VatDomesticReverseCharge,
        MarginSchemeVat,
        MarginSchemeNoVat
    ]):

        """Marking tax rate or tax exempt supply

        :param value: VatPercentage or VatExemption or VatOutOfScope or VatDomesticReverseCharge or MarginSchemeVat or MarginSchemeNoVat, vat_percentage: Applied tax rate - section 169 (j) of the VAT law, vat_exemption: Marking tax exemption -  section 169 (m) of the VAT law, vat_out_of_scope: Out of scope of the VAT law, vat_domestic_reverse_charge: Marking the national is reverse charge taxation - section 142 of the VAT law, margin_scheme_vat: Margin scheme including input tax, margin_scheme_no_vat: Margin scheme not including input tax"""
        if isinstance(value, VatPercentage):
            self.vat_percentage = float(value)
        elif isinstance(value, VatExemption):
            self.vat_exemption = str(value)
        elif isinstance(value, VatOutOfScope):
            self.vat_out_of_scope = bool(value)
        elif isinstance(value, VatDomesticReverseCharge):
            self.vat_domestic_reverse_charge = bool(value)
        elif isinstance(value, MarginSchemeVat):
            self.margin_scheme_vat = bool(value)
        elif isinstance(value, MarginSchemeNoVat):
            self.margin_scheme_no_vat = bool(value)
