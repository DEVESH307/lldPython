from lldPython.design_patterns.decoratorDPModified.pizza import Pizza

class BasePizza(Pizza):
    def __init__(self, description: str = "Base Pizza", price: float = 300.0):
        self._description = description
        self._price = price

    def get_description(self) -> str:
        """Returns the description of the base pizza."""
        return self._description

    def get_price(self) -> float:
        """Returns the cost of the base pizza."""
        return self._price

    def __str__(self) -> str:
        return f"{self.get_description()} - Price: {self.get_price()}"

