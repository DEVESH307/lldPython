from lldPython.design_patterns.factoryModified.knight import Knight, KnightV2
from lldPython.design_patterns.factoryModified.archer import Archer
from lldPython.design_patterns.factoryModified.player import Player

class CharacterFactory:
    def create_player(self, player_type):
        if player_type == "knight":
            return Knight()

        if player_type == "knightv2":
            return KnightV2()

        if player_type == "archer":
            return Archer()
