"""
References: https://github.com/faif/python-patterns/blob/master/patterns/structural/adapter.py

*What is this pattern about?

The Adapter pattern provides a different interface for a class. We can
think about it as a cable adapter that allows you to charge a phone
somewhere that has outlets in a different shape. Following this idea,
the Adapter pattern is useful to integrate classes that couldn't be
integrated due to their incompatible interfaces.

*What does this example do?

The example has classes that represent entities (Dog, Cat, Human, Car)
that make different noises. The Adapter class provides a different
interface to the original methods that make such noises. So the
original interfaces (e.g., bark and meow) are available under a
different name: make_noise.

*Where is the pattern used practically?

The Grok framework uses adapters to make objects work with a
particular API without modifying the objects themselves: http://grok.zope.org/doc/current/grok_overview.html#adapters

*References:

http://ginstrom.com/scribbles/2008/11/06/generic-adapter-class-in-python/
https://sourcemaking.com/design_patterns/adapter
http://python-3-patterns-idioms-test.readthedocs.io/en/latest/ChangeInterface.html#adapter

*TL;DR
Allows the interface of an existing class to be used as another interface.
"""

from typing import Callable, TypeVar

T = TypeVar("T")


class Dog:
    def __init__(self) -> None:
        self.name = "Dog"

    def bark(self) -> str:
        return "woof!"

    def eat(self):
        return "Bones!"


class Cat:
    def __init__(self) -> None:
        self.name = "Cat"

    def meow(self) -> str:
        return "meow!"


class Human:
    def __init__(self) -> None:
        self.name = "Human"

    def speak(self) -> str:
        return "'hello'"


class Car:
    def __init__(self) -> None:
        self.name = "Car"

    def make_noise(self, octane_level: int) -> str:
        return f"vroom{'!' * octane_level}"


class Adapter:
    """Adapts an object by replacing methods.

    Usage
    ------
    dog = Dog()
    dog = Adapter(dog, make_noise=dog.bark)
    """

    def __init__(self, obj: T, **adapted_methods: Callable):
        """We set the adapted methods in the object's dict."""
        self.obj = obj

        """Update __dict__ attribute of adapter object"""
        self.__dict__.update(adapted_methods)

    def __getattr__(self, attr):
        # print(f"__getattr__ called with arg {attr}")
        """All non-adapted calls are passed to the object."""
        return getattr(self.obj, attr)

    def original_dict(self):
        """Print original object dict."""
        return self.obj.__dict__


def main():
    dog = Dog()
    cat = Cat()
    human = Human()
    car = Car()

    dog_adapter = Adapter(dog, make_noise=dog.bark)
    cat_adapter = Adapter(cat, make_noise=cat.meow)
    human_adapter = Adapter(human, make_noise=human.speak)
    car_adapter = Adapter(car, make_noise=lambda: car.make_noise(3))

    objects = [dog_adapter, cat_adapter, human_adapter, car_adapter]

    print(dog.__dict__)
    print(dog_adapter.__dict__)
    print(dog_adapter.__dict__['obj'], dog_adapter.__dict__['make_noise'])
    print(dog_adapter.original_dict())
    print(dog.bark(), dog.eat())
    print(dog_adapter.bark(), dog_adapter.eat(), dog_adapter.make_noise())

    for obj in objects:
        print("A {0} goes {1}".format(obj.name, obj.make_noise()))


if __name__ == "__main__":
    main()
