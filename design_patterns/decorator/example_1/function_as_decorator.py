"""
https://realpython.com/primer-on-python-decorators/
"""

import functools


def simple_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """
        Do something before (actual) function call, such as,
        - caching
        - checking args and kwargs
        - logging
        - debugging
        """
        print(func, args, kwargs)
        value = func(*args, **kwargs)
        """
        Do something after the function call.
        """
        return value

    return wrapper


def decorator_with_arguments(*dargs, **dkwargs):  # noqa
    def main_decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            """
            Values of dargs (decorator argument), dkwargs (decorator keyword argument)
            """
            print(dargs, dkwargs)
            value = func(*args, **kwargs)
            return value

        return wrapper

    return main_decorator


def decorator_with_or_without_arguments(_func=None, *, num_times=2):  # noqa
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Do something here
            value = func(*args, **kwargs)
            # Do something else here
            # Use `num_times` here
            return value

        return wrapper

    if _func is None:
        return decorator
    else:
        return decorator(_func)


@decorator_with_or_without_arguments(num_times=3)
def greet(name):
    print(f"Hello {name}")


@decorator_with_or_without_arguments
def say_bye(name):
    print(f"Bye, {name}")


def meet(name):
    print(f"Hello {name}")


if __name__ == '__main__':
    greet("John Dalton!")
    say_bye("Dmitri")

    meet = decorator_with_or_without_arguments(meet)
    meet("Prem")

    meet = decorator_with_or_without_arguments()(meet)
    meet("Prem")
