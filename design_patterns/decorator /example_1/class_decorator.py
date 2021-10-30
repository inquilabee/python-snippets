"""
ALl the decorators defined in using a function or class in class_as_decorator
and function_as_decorator will work with any type of callable, including classes.

However, some of then might not behave as expected.
"""

from class_as_decorator import SimpleDecorator, ParameterisedDecorator
from function_as_decorator import simple_decorator, decorator_with_arguments


@decorator_with_arguments(3, 4)
@simple_decorator
@ParameterisedDecorator(1, 2)
@SimpleDecorator
class Animal:
    def __init__(self, name):
        self.name = name

    @simple_decorator
    def speak(self):
        return f"Animal {self.name} is saying something!"


if __name__ == '__main__':
    a = Animal(name="Doggo!")

    print(a.name, a.speak())
    print(a.name, a.speak())
    print(a.name, a.speak())
