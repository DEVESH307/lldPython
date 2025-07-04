from design_patterns.abstractFactory.Factory.AndroidCheckboxFactory import AndroidCheckboxFactory
from design_patterns.abstractFactory.UiElement.androidButton import AndroidButton

from AndroidButtonFactory import AndroidButtonFactory


class AbstractAndroidFactory:

    def create_button(self):
        return AndroidButtonFactory()

    def create_checkbox(self):
        return AndroidCheckboxFactory()
