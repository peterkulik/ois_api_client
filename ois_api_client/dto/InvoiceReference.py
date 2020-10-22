class InvoiceReference:
    """Modification or cancellation reference data

    :param original_invoice_number: Sequence number of the original invoice, on which the modification occurs - section 170 (1) c) of the VAT law
    :param modification_index: The unique sequence number referring to the original invoice
    :param modify_without_master: Indicates whether the modification references to an original invoice which is not and will not be exchanged
    """

    def __init__(self,
                 original_invoice_number: str,
                 modification_index: int,
                 modify_without_master: bool = False):
        self.original_invoice_number = original_invoice_number
        self.modify_without_master = modify_without_master
        self.modification_index = modification_index
