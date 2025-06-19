from abc import ABC, abstractmethod

class Checkbox(ABC):
    @abstractmethod
    def check(self):
        pass