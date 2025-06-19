from lldPython.design_patterns.abstractFactoryModified.factory.factoryAbc import Factory
from lldPython.design_patterns.abstractFactoryModified.uiElement.androidButton import AndroidButton

class AndroidButtonFactory(Factory):
    def create(self):
        return AndroidButton()