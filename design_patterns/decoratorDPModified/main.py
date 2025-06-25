from lldPython.design_patterns.decoratorDPModified.basePizza import BasePizza
from lldPython.design_patterns.decoratorDPModified.addons.cheese import Cheese
from lldPython.design_patterns.decoratorDPModified.addons.mushroom import Mushroom
from lldPython.design_patterns.decoratorDPModified.addons.panner import Paneer

if __name__ == '__main__':
    # pizza = BasePizza()
    # print(pizza) # Base Pizza - Price: 300.0
    #
    # cheese_pizza = Cheese(pizza)
    # print(cheese_pizza) # Base Pizza + Cheese - Price: 350.0
    #
    # mushroom_cheese_pizza = Mushroom(cheese_pizza)
    # print(mushroom_cheese_pizza) # Base Pizza + Cheese + Mushroom - Price: 380.0
    #
    # paneer_mushroom_cheese_pizza = Paneer(mushroom_cheese_pizza)
    # print(paneer_mushroom_cheese_pizza) # Base Pizza + Cheese + Mushroom + Paneer - Price: 450.0

    base = "Base Pizza"
    addons = "Cheese, Panner, Mushroom"
    addons = addons.split(", ")

    # based on the addons, we can create a pizza with the addons
    pizza = BasePizza()
    print(pizza)  # Base Pizza - Price: 300.0

    # now we can add addons to the pizza from the addons list
    for addon in addons:
        if addon == "Cheese":
            pizza = Cheese(pizza)
        elif addon == "Mushroom":
            pizza = Mushroom(pizza)
        elif addon == "Panner":
            pizza = Paneer(pizza)

    print(pizza)  # Base Pizza + Cheese + Paneer + Mushroom - Price: 450.0

    # use a builder design pattern to create the pizza with addons





