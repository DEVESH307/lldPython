from lldPython.design_patterns.factoryModified.factory import KnightFactory, KnightV2Factory, ArcherFactory
from lldPython.design_patterns.factoryModified.characterFactory import CharacterFactory

def create_player(player_type):
    if player_type == "knight":
        return KnightFactory().create_player()
    if player_type == "knightv2":
        return KnightV2Factory().create_player()
    if player_type == "archer":
        return ArcherFactory().create_player()

if __name__ == "__main__":
    player_type = input("Enter player type (knight/archer): ").strip().lower()
    player = create_player(player_type)

    if player:
        player.attack()
    else:
        print("Invalid player type!")