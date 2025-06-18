# from ..factory import KnightFactory, ArcherFactory
from lldPython.design_pattrens.Factory_Modified.factory import KnightFactory, ArcherFactory


def create_player(player_type):
    if player_type == "knight":
        return KnightFactory().create_player()
    elif player_type == "archer":
        return ArcherFactory().create_player()



if __name__ == "__main__":
    

