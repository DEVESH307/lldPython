from lldPython.design_patterns.prototypeModified.monster import Monster
import copy

class Goblin(Monster):
    def __init__(self, health=80, attack_power=15):
        self.health = health
        self.attack_power = attack_power

    def attack(self):
        return f"Goblin attacks with power {self.attack_power}!"

    def clone(self):
        return copy.deepcopy(self)