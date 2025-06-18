from lldPython.design_patterns.factoryModified.knight import Knight, KnightV2
from lldPython.design_patterns.factoryModified.archer import Archer
from abc import ABC, abstractmethod

class PlayerFactory(ABC):
    @abstractmethod
    def create_player(self):
        pass

class KnightFactory:
    def create_player(self):
        return Knight()

class ArcherFactory:
    def create_player(self):
        return Archer()
