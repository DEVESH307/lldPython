from lldPython.design_patterns.decoratorDPModified.addons.PizzaAddon import PizzaAddons


class Cheese(PizzaAddons):
    def get_description(self) -> str:
        """Returns the description of the pizza."""
        return f"{self._pizza.get_description()} + Cheese"

    def get_price(self) -> float:
        """Returns the cost of the pizza."""
        return self._pizza.get_price() + 50.0

    def __str__(self) -> str:
        return f"{self.get_description()} - Price: {self.get_price()}"