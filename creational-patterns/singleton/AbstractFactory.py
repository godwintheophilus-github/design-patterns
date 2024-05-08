from abc import ABC, abstractmethod


# Abstract Products
class Chair(ABC):
    @abstractmethod
    def sit_on(self):
        pass


class Table(ABC):
    @abstractmethod
    def place_on(self):
        pass


# Abstract Factory
class FurnitureFactory(ABC):
    @abstractmethod
    def create_chair(self) -> Chair:
        pass

    @abstractmethod
    def create_table(self) -> Table:
        pass


# Concrete Products
class ModernChair(Chair):
    def sit_on(self):
        print("Sitting on a modern chair")


class ModernTable(Table):
    def place_on(self):
        print("Placing items on a modern table")


# Concrete Factory
class ModernFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> Chair:
        return ModernChair()

    def create_table(self) -> Table:
        return ModernTable()


# Client
if __name__ == "__main__":
    factory = ModernFurnitureFactory()

    chair = factory.create_chair()
    table = factory.create_table()

    chair.sit_on()  # Output: Sitting on a modern chair
    table.place_on()  # Output: Placing items on a modern table
