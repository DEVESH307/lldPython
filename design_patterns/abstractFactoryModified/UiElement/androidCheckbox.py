from lldPython.design_patterns.abstractFactoryModified.uiElement.checkbox import Checkbox

class AndroidCheckbox(Checkbox):
    def check(self):
        print("Android Checkbox checked")