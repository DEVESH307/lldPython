from abc import ABC, abstractmethod

# kind of a contract for all bank adapters
class BankAdapterAbc(ABC):
    @abstractmethod
    def checkBalance(self):
        pass

    # other methods can be added here as needed