from lldPython.design_patterns.decoratorDPModified.pizza import Pizza

class PizzaAddons(Pizza):
    def __init__(self, pizza: Pizza):
        self._pizza = pizza

    def get_description(self) -> str:
        """Returns the description of the pizza with addons."""
        return self._pizza.get_description()

    def get_price(self) -> float:
        """Returns the cost of the pizza with addons."""
        return self._pizza.get_price()

    def __str__(self) -> str:
        return f"{self.get_description()} - Price: {self.get_price()}"