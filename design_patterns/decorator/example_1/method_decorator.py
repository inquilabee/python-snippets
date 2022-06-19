"""
Problem Statement:

Some of the methods of one or more class must accept integer arguments only.
Write a decorator to make sure the same.
"""

import functools


def ensure_integer_arguments(method):
    @functools.wraps(method)
    def wrapper(obj_ref, *args, **kwargs):
        for arg in args:
            if not isinstance(arg, int):
                raise ValueError(f"Passed positional argument {arg} which is not an integer.")

        for arg_key, arg_val in kwargs.items():
            if not isinstance(arg_val, int):
                raise ValueError(f"Passed keyword argument {arg_key}={arg_val} which is not an integer.")

        return method(obj_ref, *args, **kwargs)

    return wrapper


class NumericalOps:
    def __init__(self, val):
        self.val = val

    @ensure_integer_arguments
    def do_something_one(self, a, b, c):
        return self.val + a + b + c


if __name__ == '__main__':
    num_ops = NumericalOps(val=3)

    num_ops.do_something_one(1, 2, 4)
    num_ops.do_something_one(1, 2, c=4)
    num_ops.do_something_one(a=1, b=2, c=4)
    num_ops.do_something_one(1, 2, c="4")
