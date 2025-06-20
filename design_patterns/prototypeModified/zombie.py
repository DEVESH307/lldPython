from lldPython.design_patterns.prototypeModified.monster import Monster
import copy

class Zombie(Monster):
    def __init__(self, health=100, attack_power=10):
        self.health = health
        self.attack_power = attack_power

    def attack(self):
        return f"Zombie attacks with power {self.attack_power}!"

    def clone(self):
        return copy.deepcopy(self)