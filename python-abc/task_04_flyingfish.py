#!/usr/bin/python3
"""
Demonstration of multiple inheritance with Fish, Bird, and FlyingFish.
"""


class Fish:
    """Fish class with swimming and habitat behavior."""

    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The fish lives in water")


class Bird:
    """Bird class with flying and habitat behavior."""

    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """FlyingFish inherits from both Fish and Bird."""

    def swim(self):
        print("The flying fish is swimming!")

    def fly(self):
        print("The flying fish is soaring!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")


if __name__ == "__main__":
    f = Fish()
    b = Bird()
    ff = FlyingFish()

    f.swim()
    f.habitat()

    b.fly()
    b.habitat()

    ff.swim()
    ff.fly()
    ff.habitat()
