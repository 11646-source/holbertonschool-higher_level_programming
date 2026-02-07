#!/usr/bin/python3
"""
Example showing abstract base class Animal
with Dog and Cat subclasses.
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class for animals."""

    @abstractmethod
    def sound(self):
        """Abstract method that must be implemented by subclasses."""
        pass


class Dog(Animal):
    """Dog subclass implementing sound method."""

    def sound(self):
        return "Bark"


class Cat(Animal):
    """Cat subclass implementing sound method."""

    def sound(self):
        return "Meow"


if __name__ == "__main__":
    dog = Dog()
    cat = Cat()

    print(dog.sound())
    print(cat.sound())

