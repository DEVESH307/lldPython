from lldPython.design_patterns.abstractFactoryModified.factory.factoryAbc import Factory
from lldPython.design_patterns.abstractFactoryModified.uiElement.iosButton import IOSButton

class IOSButtonFactory(Factory):
    def create(self):
        return IOSButton()