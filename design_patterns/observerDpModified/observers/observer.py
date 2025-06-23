from abc import ABC, abstractmethod

from lldPython.design_patterns.observerDpModified.subject.subject import Subject


class Observer(ABC):
    def register_subject(self, subject: Subject):
        subject.register(self)

    def unregister_subject(self, subject: Subject):
        subject.unregister(self)

    @abstractmethod
    def update(self, temperature, humidity):
        pass