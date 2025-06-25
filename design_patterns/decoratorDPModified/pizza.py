from abc import ABC, abstractmethod


class Pizza(ABC):
    @abstractmethod
    def get_description(self) -> str:
        """Returns the description of the pizza."""
        pass

    @abstractmethod
    def get_price(self) -> float:
        """Returns the cost of the pizza."""
        pass