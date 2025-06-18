from design_patterns.abstractFactory.Factory.AbstractAndroidFactory import AbstractAndroidFactory
from design_patterns.abstractFactory.Factory.AndroidButtonFactory import AndroidButtonFactory
from design_patterns.abstractFactory.Factory.OSFactory import OSFactory


def Deploy(val):

    Abs = OSFactory("Android")
    Button = Abs.create_button().create()
    Button.click()
    Checkbox = Abs.create_checkbox().create()
    Checkbox.click()


if __name__ == '__main__':
    Deploy()
