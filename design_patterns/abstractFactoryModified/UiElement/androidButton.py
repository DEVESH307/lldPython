from lldPython.design_patterns.abstractFactoryModified.uiElement.button import Button

class AndroidButton(Button):
    def click(self):
        print("Android Button clicked")