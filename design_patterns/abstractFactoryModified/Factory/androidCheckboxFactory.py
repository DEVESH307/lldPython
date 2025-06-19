from lldPython.design_patterns.abstractFactoryModified.factory.factoryAbc import Factory
from lldPython.design_patterns.abstractFactoryModified.uiElement.androidCheckbox import AndroidCheckbox


class AndroidCheckboxFactory(Factory):
    def create(self):
        return AndroidCheckbox()