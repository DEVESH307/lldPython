from lldPython.design_patterns.abstractFactoryModified.factory.abstractAndroidFactory import AbstractAndroidFactory
from lldPython.design_patterns.abstractFactoryModified.factory.abstractIOSFactory import AbstractIOSFactory

class OSFactory:
    def decide(self, val):
        if val == "android":
            return AbstractAndroidFactory()
        if val == "ios":
            return AbstractIOSFactory()