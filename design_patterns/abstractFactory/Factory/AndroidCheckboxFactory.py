from FactoryAbc import Factory
from design_patterns.abstractFactory.UiElement.AndroidCheckbox import  Checkbox


class AndroidCheckboxFactory(Factory):
    def create(self):
        return Checkbox()
