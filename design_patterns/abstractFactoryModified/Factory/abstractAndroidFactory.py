from lldPython.design_patterns.abstractFactoryModified.uiElement.androidButton import AndroidButton
from lldPython.design_patterns.abstractFactoryModified.factory.androidCheckboxFactory import AndroidCheckboxFactory
from lldPython.design_patterns.abstractFactoryModified.factory.androidButtonFactory import AndroidButtonFactory
from lldPython.design_patterns.abstractFactoryModified.factory.androidCheckboxFactory import AndroidCheckboxFactory


class AbstractAndroidFactory:
    def create_button(self):
        return AndroidButtonFactory()

    def create_checkbox(self):
        return AndroidCheckboxFactory()