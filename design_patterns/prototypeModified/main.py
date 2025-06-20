from lldPython.design_patterns.prototypeModified.zombie import Zombie
from lldPython.design_patterns.prototypeModified.goblin import Goblin
from lldPython.design_patterns.prototypeModified.vampire import Vampire

if __name__ == '__main__':
    # Create instances of monsters
    zombie = Zombie(100, 10)
    goblin = Goblin(80, 15)
    vampire = Vampire(120, 20)

    # Clone the monsters
    arrZombie = []
    arrGoblin = []
    arrVampire = []

    for _ in range(100):
        arrZombie.append(zombie.clone())
        arrGoblin.append(goblin.clone())
        arrVampire.append(vampire.clone())

    arrZombie[0] = Zombie(99, 9)  # Change the first zombie's health and attack power
    arrGoblin[0] = Goblin(79, 14)  # Change the first goblin's health and attack power
    arrVampire[0] = Vampire(70, 15) # Change the first vampire's health and attack power

    print(arrZombie[0].health, arrZombie[0].attack_power)
    print(arrZombie[0].attack())
    print(arrZombie[1].health, arrZombie[1].attack_power)
    print(arrZombie[1].attack())
    print(arrGoblin[1].health, arrGoblin[1].attack_power)
    print(arrVampire[2].health, arrVampire[2].attack_power)
