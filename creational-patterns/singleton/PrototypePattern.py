from abc import ABC, abstractmethod
import copy


class Prototype(ABC):
    @abstractmethod
    def createSample():
        pass


class Product(Prototype):
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def createSample(self):
        return copy.deepcopy(self)

    def __str__(self):
        return f"{self.name}-{self.category}"


if __name__ == "__main__":
    originalProduct = Product("godwin", "human")
    print(originalProduct)
    prototypeProduct = originalProduct.createSample()
    print(prototypeProduct)
