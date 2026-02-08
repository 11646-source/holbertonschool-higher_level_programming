#!/usr/bin/python3
"""
Demonstration of mixins with SwimMixin, FlyMixin, and Dragon.
"""


class SwimMixin:
    """Mixin providing swimming ability."""

    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """Mixin providing flying ability."""

    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon inherits both swimming and flying abilities."""

    def roar(self):
        print("The dragon roars!")


if __name__ == "__main__":
    draco = Dragon()
    draco.swim()
    draco.fly()
    draco.roar()
