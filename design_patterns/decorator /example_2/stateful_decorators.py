import functools


def count_calls(func):
    @functools.wraps(func)
    def wrapper_count_calls(*args, **kwargs):
        wrapper_count_calls.num_calls += 1
        print(f"Call {wrapper_count_calls.num_calls} of {func.__name__!r}")
        return func(*args, **kwargs)

    wrapper_count_calls.num_calls = 0  # function attribute
    return wrapper_count_calls


class CountCalls:
    def __init__(self, func):
        functools.update_wrapper(self, func)  # Update Wrapper
        self.func = func
        self.num_calls = 0  # create state

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"Call {self.num_calls} of {self.func.__name__!r}")
        return self.func(*args, **kwargs)


@CountCalls
def say_meow():
    print("Meow!")


@count_calls
def say_whee():
    print("Whee!")


if __name__ == '__main__':
    say_whee()
    say_whee()
    say_whee()
    say_whee()

    say_meow()
    say_meow()
    say_meow()
    say_meow()
