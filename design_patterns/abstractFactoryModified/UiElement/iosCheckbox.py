from lldPython.design_patterns.abstractFactoryModified.uiElement.checkbox import Checkbox

class IOSCheckbox(Checkbox):
    def check(self):
        print("IOS Checkbox checked")