from FactoryAbc import Factory
from design_patterns.abstractFactory.UiElement.IosButton import IosButton


class IosButtonFactory(Factory):

    def create(self):
        return IosButton()
