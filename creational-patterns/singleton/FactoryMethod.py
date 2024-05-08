from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return "Woof"


class Cat(Animal):
    def speak(self):
        return "Meow"


class AnimalShop(ABC):  # Animal Factory Method
    @abstractmethod
    def viewAnimal(self):
        pass


class DogShop(AnimalShop):
    def viewAnimal(self):
        return Dog()


class CatShop(AnimalShop):
    def viewAnimal(self):
        return Cat()


class AnimalClient:
    def __init__(self, shop):
        self.shop = shop

    def getAnimalSound(self):
        return self.shop.viewAnimal().speak()


if __name__ == "__main__":
    dogShop = DogShop()
    animalClient = AnimalClient(dogShop)
    print(animalClient.getAnimalSound())
