from archer import Archer
from factory import PlayerFactory
from knight import Knight


class CharacterFactory:
    def create_player(self, player_type):
        if player_type == 'Knight':
            return Knight()

        if player_type == 'Archer':
            return Archer()

