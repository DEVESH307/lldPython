from lldPython.design_patterns.factoryModified.player import Player

class Archer(Player):
    def attack(self):
        print("Archer attacks with bow and arrow!")