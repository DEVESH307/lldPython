from ComputerDirector import ComputerDirector
from GamingComputerBuilder import GamingComputerBuilder

if __name__ == "__main__":
    gcb = GamingComputerBuilder()
    director = ComputerDirector(gcb)
    director.construct_computer()
    computer = director.build_computer()

    print(computer)