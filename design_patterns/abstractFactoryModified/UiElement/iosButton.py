from lldPython.design_patterns.abstractFactoryModified.uiElement.button import Button

class IOSButton(Button):
    def click(self):
        print("IOS Button clicked")