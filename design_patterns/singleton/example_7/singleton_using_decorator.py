"""
Reference: RealPython Blog
"""

import functools


def singleton(cls):
    """Make a class a Singleton class (only one instance)"""

    @functools.wraps(cls)
    def wrapper_singleton(*args, **kwargs):
        if not wrapper_singleton.instance:
            wrapper_singleton.instance = cls(*args, **kwargs)
        return wrapper_singleton.instance

    wrapper_singleton.instance = None  # function attributes, huh?
    return wrapper_singleton


@singleton
class TheOne:
    def fun(self):  # noqa
        return "I'm having fun"


@singleton
class TheOtherOne:
    def fun(self):  # noqa
        return "I'm having fun"


if __name__ == '__main__':
    first = TheOne()
    second = TheOne()

    third = TheOtherOne()
    fourth = TheOtherOne()

    print(first is second, first.fun())
    print(third is second)
    print(third is fourth)
