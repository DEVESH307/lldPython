from lldPython.design_patterns.decoratorDPModified.addons.PizzaAddon import PizzaAddons


class Paneer(PizzaAddons):
    def get_description(self) -> str:
        """Returns the description of the pizza."""
        return f"{self._pizza.get_description()} + Paneer"

    def get_price(self) -> float:
        """Returns the cost of the pizza."""
        return self._pizza.get_price() + 70.0

    def __str__(self) -> str:
        return f"{self.get_description()} - Price: {self.get_price()}"
