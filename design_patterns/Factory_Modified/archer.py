from lldPython.design_patterns.Factory_Modified.player import Player

class Archer(Player):
    def attack(self):
        print("Archer attacks with bow and arrow!")