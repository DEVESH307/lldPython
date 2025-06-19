from lldPython.design_patterns.abstractFactoryModified.factory.factoryAbc import Factory
from lldPython.design_patterns.abstractFactoryModified.uiElement.iosCheckbox import IOSCheckbox

class IOSCheckboxFactory(Factory):
    def create(self):
        return IOSCheckbox()
