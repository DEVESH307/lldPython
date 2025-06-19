from lldPython.design_patterns.abstractFactoryModified.uiElement.iosButton import IOSButton
from lldPython.design_patterns.abstractFactoryModified.uiElement.iosCheckbox import IOSCheckbox
from lldPython.design_patterns.abstractFactoryModified.factory.iosCheckboxFactory import IOSCheckboxFactory
from lldPython.design_patterns.abstractFactoryModified.factory.iosButtonFactory import IOSButtonFactory

class AbstractIOSFactory:
    def create_button(self):
        return IOSButtonFactory()

    def create_checkbox(self):
        return IOSCheckboxFactory()