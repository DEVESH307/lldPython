from lldPython.design_patterns.abstractFactoryModified.factory.osFactory import OSFactory
from lldPython.design_patterns.abstractFactoryModified.factory.abstractAndroidFactory import AbstractAndroidFactory
from lldPython.design_patterns.abstractFactoryModified.factory.abstractIOSFactory import AbstractIOSFactory

# def deploy(val):
#     if val == "android":
#         factory = AbstractAndroidFactory()
#     elif val == "ios":
#         factory = AbstractIOSFactory()
#     else:
#         print("Invalid OS type.")
#         return
#
#     button = factory.create_button().create()
#     button.click()
#
#     checkbox = factory.create_checkbox().create()
#     checkbox.check()

def deploy(val):
    factory = OSFactory().decide(val)
    if not factory:
        print("Invalid OS type.")
        return
    button = factory.create_button().create()
    button.click()
    checkbox = factory.create_checkbox().create()
    checkbox.check()

if __name__ == "__main__":
    deploy(input("Enter OS type (Android/IOS): ").strip().lower())
