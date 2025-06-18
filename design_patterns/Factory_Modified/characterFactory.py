from lldPython.design_patterns.Factory_Modified.knight import Knight, KnightV2
from lldPython.design_patterns.Factory_Modified.archer import Archer
from lldPython.design_patterns.Factory_Modified.player import Player

class CharacterFactory:
    def create_player(self, player_type):
        if player_type == "knight":
            return Knight()

        if player_type == "archer":
            return Archer()
