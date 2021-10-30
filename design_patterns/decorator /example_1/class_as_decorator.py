"""
Examples of class being used as a decorator, not to be confused with class decorator.

References:
    https://levelup.gitconnected.com/mastering-decorators-in-python-3-588cb34fff5e
"""

import functools


class SimpleDecorator:
    def __init__(self, func):
        functools.update_wrapper(
            wrapper=self,
            wrapped=func
        )

        """save function"""
        self.func = func

        """Define additional instance variables, if needed."""
        self.num_calls = 0

    def __call__(self, *args, **kwargs):  # Acts as wrapper function
        self.num_calls += 1
        print(f"Call {self.num_calls} of {self.func.__name__!r} starting.")
        value = self.func(*args, **kwargs)
        print(f"Call {self.num_calls} of {self.func.__name__!r} finished.")
        return value


class ParameterisedDecorator:

    def __init__(self, *decorator_args, **decorator_kwargs):
        # save arguments passed to class here, if needed.
        print(f"inside __init__() with input function with args {decorator_args} and kwargs {decorator_kwargs}")

    def __call__(self, f):
        print(f"inside __call__() with function {f.__name__}")

        @functools.wraps(f)
        def wrapped(*args, **kwargs):
            print(f"inside wrapped with args {args} and kwargs {kwargs}")
            return f(*args, **kwargs)

        return wrapped


@SimpleDecorator
def say_whee():
    print("Whee!")


def say_hi(name):
    print(f"Hi, {name}!")


def say_bye(name):
    print(f"Bye, {name}!")


@ParameterisedDecorator(received_from="Python", written_with="Love")
def never_say_bye(name):
    print(f"We will meet again, {name}!")


@ParameterisedDecorator()  # Notice the parenthesis after decorator name
def life_is_beautiful(name):
    print(f"Life is beautiful, {name}!")


if __name__ == '__main__':
    say_whee()
    say_whee()
    say_whee()

    say_hi = SimpleDecorator(say_hi)

    say_hi("Alice")
    say_hi("Bob")
    say_hi("Charles")

    say_bye = ParameterisedDecorator(1, 2)(say_bye)

    say_bye("Alice")
    say_bye("Bob")
    say_bye("Charles")

    never_say_bye("Alice")
    never_say_bye("Bob")
    never_say_bye("Charles")

    life_is_beautiful("Alice")
    life_is_beautiful("Bob")
    life_is_beautiful("Charles")
