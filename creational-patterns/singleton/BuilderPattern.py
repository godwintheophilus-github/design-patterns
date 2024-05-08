class Computer:
    def __init__(self, case, motherboard, cpu, memory, storage):
        self.case = case
        self.motherboard = motherboard
        self.cpu = cpu
        self.memory = memory
        self.storage = storage


class ComputerBuilder:
    def __init__(self):
        self.computer = Computer("", "", "", "", "")

    def setCase(self, case):
        self.computer.case = case
        return self

    def setMotherboard(self, motherboard):
        self.computer.motherboard = motherboard
        return self

    def setCpu(self, cpu):
        self.computer.cpu = cpu
        return self

    def setMemory(self, memory):
        self.computer.memory = memory
        return self

    def setStorage(self, storage):
        self.computer.storage = storage
        return self

    def build(self):
        return {
            "computer": {
                "case": self.computer.case,
                "cpu": self.computer.cpu,
                "memory": self.computer.memory,
                "storage": self.computer.storage,
                "motherboard": self.computer.motherboard,
            }
        }


if __name__ == "__main__":
    builder = ComputerBuilder()
    computer = (
        builder.setCase("Zenon")
        .setCpu("1000m")
        .setMemory("16gb")
        .setMotherboard("XZ")
        .setStorage("1TB")
        .build()
    )

    print(computer)
