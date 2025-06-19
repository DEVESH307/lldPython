class ComputerDirector:
    def __init__(self, ComputerBuilder):
        self.computerBuilder = ComputerBuilder

    def construct_computer(self):
        # set the specifications for a gaming computer as per customer requirements
        self.computerBuilder.set_ram(8)
        # self.computerBuilder.set_cpu(1)
        self.computerBuilder.set_cpu(2)
        self.computerBuilder.set_gpu("NVIDIA RTX 3080")
        self.computerBuilder.set_storage(1000)
        self.computerBuilder.set_power_supply(750)

    def build_computer(self):
        return self.computerBuilder.build()