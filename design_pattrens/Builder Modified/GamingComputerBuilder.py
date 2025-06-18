from ComputerBuilder import ComputerBuilder
from Computer import Computer

class GamingComputerBuilder(ComputerBuilder):
    def __init__(self):
        self.ram = None
        self.cpu = None
        self.gpu = None
        self.storage = 0
        self.power_supply = 0

    def set_ram(self, ram):
        self.ram = ram

    def set_cpu(self, cpu):
        if cpu < 2:
            raise ValueError("CPU must be at least 2")
        self.cpu = cpu

    def set_gpu(self, gpu):
        self.gpu = gpu

    def set_storage(self, storage):
        self.storage = storage

    def set_power_supply(self, power_supply):
        self.power_supply = power_supply

    def build(self):
        c = Computer()
        c.set_ram(self.ram)
        c.set_cpu(self.cpu)
        c.set_gpu(self.gpu)
        c.set_storage(self.storage)
        c.set_power_supply(self.power_supply)
        return c