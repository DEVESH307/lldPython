from FactoryAbc import Factory
from design_patterns.abstractFactory.UiElement.androidButton import AndroidButton


class AndroidButtonFactory(Factory):
    def create(self):
        return AndroidButton()
