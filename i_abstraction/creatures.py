from abc import ABC, abstractmethod

'''
Example of an abstract class and two concrete subclasses
'''
class Animal(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def make_sound(self) -> str:
        pass


class Dog(Animal):
    def __init__(self, name: str):
        super().__init__(name)

    def make_sound(self) -> str:
        return "Bark!"


class Cat(Animal):
    def __init__(self, name: str):
        super().__init__(name)

    def make_sound(self) -> str:
        return "Meow!"


if __name__ == "__main__":
    dog = Dog("Fido")
    cat = Cat("Evil")
    print(dog.make_sound())
    print(cat.make_sound())

    animals = [dog, cat]
    for creature in animals:
        print(creature.make_sound())
