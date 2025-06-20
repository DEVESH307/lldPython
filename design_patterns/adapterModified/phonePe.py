class PhonePe:
    def __init__(self, Adapter):
        self.Adapter = Adapter

    def checkBalance(self):
        return self.Adapter.checkBalance()