class Singleton(type):
    """Metaclass which can be inherited as "metaclass=Singleton" to make a class a Singleton class"""

    _instances = {}  # dictionary of class and their instances

    def __call__(cls, *args, **kwargs):
        print(f"__call__ call")
        print(cls, *args, **kwargs)
        if cls not in cls._instances:
            print("__call__: before super call")
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
            print("__call__: after super call")
        return cls._instances[cls]


class SingletonClass(metaclass=Singleton):
    def __init__(self, a, b):
        print(f"instance __init__ call")
        self.a = a
        self.b = b

    def __call__(self, *args, **kwargs):
        """This is different from __call__ of metaclass"""
        print("instance __call__ call")
        print(*args, **kwargs)


class AnotherClass(metaclass=Singleton):
    pass


if __name__ == '__main__':
    x = SingletonClass(2, 3)
    print()
    y = SingletonClass(4, 5)

    print(x == y, x is y)
    print(y.a, y.b)

    z = AnotherClass()
    w = AnotherClass()

    print(z == w, z is w)

    print(x is z)

    print(Singleton._instances)  # noqa
