from lldPython.design_patterns.factoryModified.characterFactory import CharacterFactory
from lldPython.design_patterns.factoryModified.factory import KnightFactory, ArcherFactory

def create_player(val_from_player):
    player = CharacterFactory().create_player(val_from_player)
    if player:
        player.attack()
    else:
        print("Invalid player type!")


if __name__ == '__main__':
    # create_player("knight")
    # create_player("archer")
    player_type = input("Enter player type (knight/archer): ").strip().lower()
    player = create_player(player_type)
