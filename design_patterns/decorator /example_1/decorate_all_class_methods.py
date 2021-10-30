from datetime import datetime
from functools import wraps
import time
from contextlib import suppress


def time_this(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        before = datetime.now()
        x = func(*args, **kwargs)
        after = datetime.now()
        print(f"** elapsed Time = {after - before} **")
        return x

    return wrapped


def time_all_class_methods(cls):
    class Wrapper:
        def __init__(self, *args, **kwargs):
            self.decorated_obj = cls(*args, **kwargs)

        def __getattribute__(self, s):
            with suppress(AttributeError):
                x = super().__getattribute__(s)
                return x

            x = self.decorated_obj.__getattribute__(s)

            # if isinstance(x, self.__init__):
            #     pass

            if type(x) is type(self.__init__):
                # it is an instance method
                print(f"attribute belonging to decorated_obj: {s}")
                return time_this(x)
            else:
                return x

    return Wrapper


@time_all_class_methods
class MyClass:
    def __init__(self):
        time.sleep(1.8)

    def method_x(self):
        time.sleep(0.7)

    def method_y(self):
        time.sleep(1.2)


if __name__ == '__main__':
    instance = MyClass()
    instance.method_x()
    instance.method_y()
