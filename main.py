from abc import ABC, abstractmethod

# Product interface
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

# Concrete Products
class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Creator
class AnimalFactory(ABC):
    @abstractmethod
    def create_animal(self):
        pass

# Concrete Creators
class DogFactory(AnimalFactory):
    def create_animal(self):
        return Dog()

class CatFactory(AnimalFactory):
    def create_animal(self):
        return Cat()

# Client
class PetStore:
    def __init__(self, animal_factory):
        self.animal_factory = animal_factory

    def show_pet(self):
        animal = self.animal_factory.create_animal()
        print(f"Hello, I'm {animal.__class__.__name__}! {animal.speak()}")

# Usage
if __name__ == "__main__":
    dog_factory = DogFactory()
    cat_factory = CatFactory()

    store1 = PetStore(dog_factory)
    store1.show_pet()

    store2 = PetStore(cat_factory)
    store2.show_pet()
