class InvoiceReference:
    """Modification or cancellation reference data

    :param original_invoice_number: Sequence number of the original invoice, on which the modification occurs - section 170 (1) c) of the VAT law
    :param modify_without_master: Indicates whether the modification references to an original invoice which is not and will not be exchanged
    :param modification_index: The unique sequence number referring to the original invoice
    """

    def __init__(self, original_invoice_number, modify_without_master, modification_index):
        self.original_invoice_number = original_invoice_number
        self.modify_without_master = modify_without_master
        self.modification_index = modification_index
