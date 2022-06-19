class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


class SingletonClass(Singleton):
    pass


class AnotherClass(Singleton):
    pass


if __name__ == '__main__':
    x = SingletonClass()
    y = SingletonClass()

    z = AnotherClass()
    w = AnotherClass()

    print(x == y, x is y)
    print(z == w, z is w)

    print(x is z)
