from lldPython.design_patterns.Factory_Modified.player import Player

class Knight(Player):
    def attack(self):
        print("Knight attacks with sword!")

class KnightV2(Player):
    def attack(self):
        print("Knight2 attacks with sword++!")