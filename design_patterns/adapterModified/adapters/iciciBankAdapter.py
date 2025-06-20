from lldPython.design_patterns.adapterModified.banks.iciciBank import IciciBank
from lldPython.design_patterns.adapterModified.adapters.bankAdapterAbc import BankAdapterAbc

class IciciBankAdapter(BankAdapterAbc):
    def __init__(self):
        self.bank = IciciBank()

    def checkBalance(self):
        return self.bank.balance()