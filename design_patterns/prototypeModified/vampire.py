from lldPython.design_patterns.prototypeModified.monster import Monster
import copy

class Vampire(Monster):
    def __init__(self, health=120, attack_power=20):
        self.health = health
        self.attack_power = attack_power

    def attack(self):
        return f"Vampire attacks with power {self.attack_power}!"

    def clone(self):
        return copy.deepcopy(self)