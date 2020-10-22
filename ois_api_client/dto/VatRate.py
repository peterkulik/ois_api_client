class VatRate:
    """Marking tax rate or tax exempt supply

    :param vat_percentage: Applied tax rate - section 169 (j) of the VAT law
    :param vat_exemption: Marking tax exemption -  section 169 (m) of the VAT law
    :param vat_out_of_scope: Out of scope of the VAT law
    :param vat_domestic_reverse_charge: Marking the national is reverse charge taxation - section 142 of the VAT law
    :param margin_scheme_vat: Margin scheme including input tax
    :param margin_scheme_no_vat: Margin scheme not including input tax
    """

    def __init__(self,
                 vat_percentage: float,
                 vat_exemption: str,
                 vat_out_of_scope: bool = False,
                 vat_domestic_reverse_charge: bool = False,
                 margin_scheme_vat: bool = False,
                 margin_scheme_no_vat: bool = False):
        self.vat_percentage = vat_percentage
        self.vat_exemption = vat_exemption
        self.vat_out_of_scope = vat_out_of_scope
        self.vat_domestic_reverse_charge = vat_domestic_reverse_charge
        self.margin_scheme_vat = margin_scheme_vat
        self.margin_scheme_no_vat = margin_scheme_no_vat
