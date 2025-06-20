from lldPython.design_patterns.adapterModified.banks.yesBank import YesBank
from lldPython.design_patterns.adapterModified.adapters.bankAdapterAbc import BankAdapterAbc

class YesBankAdapter(BankAdapterAbc):
    def __init__(self):
        self.bank = YesBank()

    def checkBalance(self):
        return self.bank.balance()